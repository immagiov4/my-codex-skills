# My Codex skills

This repository contains the Codex skills I use across local machines and cloud environments.

The collection combines my own workflows with adapted work from public skill repositories. The adaptations remove host-specific commands, keep authorization boundaries explicit, and use Codex skill metadata. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for attribution.

## Install as a Codex plugin

```bash
codex plugin marketplace add immagiov4/my-codex-skills
codex plugin add my-codex-skills@my-codex-skills
```

Start a new Codex task after installation so Codex discovers the skills.

## Install from a clone

Clone the repository and run the script for your operating system.

Linux and macOS:

```bash
git clone https://github.com/immagiov4/my-codex-skills.git
cd my-codex-skills
./scripts/install.sh
```

Windows PowerShell:

```powershell
git clone https://github.com/immagiov4/my-codex-skills.git
Set-Location my-codex-skills
.\scripts\install.ps1
```

The scripts copy `skills/` into `$CODEX_HOME/skills`. If `CODEX_HOME` is unset, they use the default `.codex/skills` directory in the user profile. Existing files with the same names are overwritten. Files removed from this repository are not deleted from the destination.

## Update

Pull the repository and run the install script again. For plugin installations, update or reinstall the plugin through Codex.

## Contents

Each directory under `skills/` is an independently discoverable Codex skill. The repository also includes a plugin manifest, so the complete collection can be installed without copying directories by hand.

`web-performance` measures browser-facing performance when runtime evidence is available. When it only has source code, it reports possible performance effects without pretending that static analysis measured Core Web Vitals.

`problem-to-github-issue` checks requirements against `AGENTS.md` and maintainer decisions before creating or rewriting an issue. Acceptance criteria describe the approved change; they do not add requirements.

`receiving-pr-reviews` validates the issue and PR contract before investigating review findings. Repository instructions take precedence over conflicting review comments; unresolved conflicts in the original requirements go to the maintainer.

## License

Original work and local adaptations are released under the MIT License. Upstream material remains covered by its original license and copyright notice.
