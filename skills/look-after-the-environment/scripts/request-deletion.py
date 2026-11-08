"""Ask the desktop user to delete one directory from the recovery store."""

import argparse
from concurrent.futures import ThreadPoolExecutor
import os
from pathlib import Path
import shutil
import stat
import tkinter as tk
from tkinter import messagebox, ttk


RECOVERY_ROOT = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")).absolute() / "worktree-recovery"
PROGRESS_INTERVAL_MS = 80


def directory_identity(target, recovery_root):
    if not target.is_absolute() or target.parent != recovery_root or target.name == "..":
        raise ValueError("Scegli una cartella direttamente nel deposito di recupero.")

    for directory in (*reversed(target.parents), target):
        info = directory.lstat()
        if not stat.S_ISDIR(info.st_mode) or info.st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT:
            raise ValueError(f"Il percorso contiene un collegamento o non è una cartella: {directory}")
    return info.st_dev, info.st_ino, info.st_ctime_ns


def show_request(window, target, reason, recovery_root=RECOVERY_ROOT):
    identity = directory_identity(target, recovery_root)
    window.title("Conferma eliminazione")
    window.resizable(False, False)

    panel = ttk.Frame(window, padding=20)
    panel.grid()
    ttk.Label(panel, text="Eliminare definitivamente questa cartella?").grid(sticky="w")
    ttk.Label(panel, text=str(target), wraplength=560).grid(sticky="w", pady=10)
    ttk.Label(panel, text=reason, wraplength=560).grid(sticky="w", pady=(0, 16))

    result = "rifiutata"

    def delete_directory():
        if directory_identity(target, recovery_root) != identity:
            raise ValueError("La cartella è cambiata. Serve una nuova richiesta.")
        shutil.rmtree(target)
        if target.exists():
            raise OSError("La cartella è ancora presente.")

    def finish_when_ready(deletion):
        nonlocal result
        if not deletion.done():
            window.after(PROGRESS_INTERVAL_MS, finish_when_ready, deletion)
            return
        progress.stop()
        try:
            deletion.result()
        except (OSError, ValueError) as error:
            result = "errore"
            messagebox.showerror("Eliminazione non completata", str(error), parent=window)
        else:
            result = "eliminata"
        window.destroy()

    def approve():
        reject.state(["disabled"])
        approval.state(["disabled"])
        window.protocol("WM_DELETE_WINDOW", lambda: None)
        status.configure(text="Eliminazione in corso…")
        progress.grid(sticky="ew", pady=(0, 12))
        progress.start(PROGRESS_INTERVAL_MS)
        finish_when_ready(executor.submit(delete_directory))

    status = ttk.Label(panel)
    status.grid(sticky="w")
    progress = ttk.Progressbar(panel, mode="indeterminate")
    buttons = ttk.Frame(panel)
    buttons.grid(sticky="e")
    reject = ttk.Button(buttons, text="Rifiuta", command=window.destroy)
    reject.pack(side="left", padx=(0, 8))
    approval = ttk.Button(buttons, text="Approva", command=approve)
    approval.pack(side="left")
    window.protocol("WM_DELETE_WINDOW", window.destroy)
    reject.focus_set()
    with ThreadPoolExecutor(max_workers=1) as executor:
        window.mainloop()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path)
    parser.add_argument("--reason", required=True)
    args = parser.parse_args()
    try:
        result = show_request(tk.Tk(), args.target, args.reason)
    except (OSError, ValueError, tk.TclError) as error:
        parser.exit(1, f"errore: {error}\n")
    print(f"{result}: {args.target}", flush=True)
    return int(result == "errore")


if __name__ == "__main__":
    raise SystemExit(main())
