import { defineConfig } from 'vite';

export default defineConfig({
  base: '/',
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    cssCodeSplit: false,
    rollupOptions: {
      output: {
        entryFileNames: 'main.js',
        assetFileNames: asset => asset.names.some(name => name.endsWith('.css')) ? 'style.css' : 'assets/[name]-[hash][extname]',
      },
    },
  },
});
