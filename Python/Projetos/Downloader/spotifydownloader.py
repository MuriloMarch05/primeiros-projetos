import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import subprocess
import sys
import os
from pathlib import Path
import json

class SpotifyDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("Spotify Downloader Pro")
        self.root.geometry("700x650")
        self.root.resizable(False, False)
        
        # Variáveis
        self.download_path = tk.StringVar(value=str(Path.home() / "Downloads" / "Spotify"))
        self.url_var = tk.StringVar()
        self.is_downloading = False
        self.spotdl_path = None
        
        # Configurar estilo
        self.setup_style()
        
        # Criar interface
        self.create_widgets()
        
        # Verificar dependências na inicialização
        self.root.after(100, self.check_dependencies)
    
    def setup_style(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Cores do Spotify
        bg_color = "#191414"
        fg_color = "#FFFFFF"
        accent_color = "#1DB954"
        
        self.root.configure(bg=bg_color)
        
        style.configure("TFrame", background=bg_color)
        style.configure("TLabel", background=bg_color, foreground=fg_color, font=("Arial", 10))
        style.configure("Title.TLabel", font=("Arial", 16, "bold"), foreground=accent_color)
        style.configure("TButton", font=("Arial", 10, "bold"), borderwidth=0)
        style.map("TButton", background=[("active", accent_color)])
        style.configure("Accent.TButton", background=accent_color, foreground="white")
    
    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = ttk.Label(main_frame, text="🎵 Spotify Downloader Pro", 
                                style="Title.TLabel")
        title_label.pack(pady=(0, 20))
        
        # Frame de URL
        url_frame = ttk.Frame(main_frame)
        url_frame.pack(fill=tk.X, pady=10)
        
        url_label = ttk.Label(url_frame, text="URL do Spotify:")
        url_label.pack(anchor=tk.W)
        
        url_entry = ttk.Entry(url_frame, textvariable=self.url_var, font=("Arial", 10))
        url_entry.pack(fill=tk.X, pady=(5, 0))
        
        hint_label = ttk.Label(url_frame, 
                               text="Cole o link de uma música, álbum ou playlist do Spotify",
                               font=("Arial", 8), foreground="#B3B3B3")
        hint_label.pack(anchor=tk.W, pady=(2, 0))
        
        # Frame de destino
        dest_frame = ttk.Frame(main_frame)
        dest_frame.pack(fill=tk.X, pady=10)
        
        dest_label = ttk.Label(dest_frame, text="Pasta de destino:")
        dest_label.pack(anchor=tk.W)
        
        dest_path_frame = ttk.Frame(dest_frame)
        dest_path_frame.pack(fill=tk.X, pady=(5, 0))
        
        dest_entry = ttk.Entry(dest_path_frame, textvariable=self.download_path, 
                               font=("Arial", 9), state="readonly")
        dest_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        browse_btn = ttk.Button(dest_path_frame, text="Procurar", 
                                command=self.browse_folder, width=10)
        browse_btn.pack(side=tk.LEFT, padx=(5, 0))
        
        # Opções de download
        options_frame = ttk.LabelFrame(main_frame, text="Opções", padding="10")
        options_frame.pack(fill=tk.X, pady=10)
        
        self.format_var = tk.StringVar(value="mp3")
        self.quality_var = tk.StringVar(value="320")
        
        format_label = ttk.Label(options_frame, text="Formato:")
        format_label.grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        
        format_combo = ttk.Combobox(options_frame, textvariable=self.format_var,
                                    values=["mp3", "m4a", "flac", "opus"],
                                    state="readonly", width=10)
        format_combo.grid(row=0, column=1, sticky=tk.W)
        
        quality_label = ttk.Label(options_frame, text="Qualidade:")
        quality_label.grid(row=0, column=2, sticky=tk.W, padx=(20, 10))
        
        quality_combo = ttk.Combobox(options_frame, textvariable=self.quality_var,
                                     values=["128", "192", "256", "320"],
                                     state="readonly", width=10)
        quality_combo.grid(row=0, column=3, sticky=tk.W)
        
        # Botões
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        self.download_btn = tk.Button(button_frame, text="⬇ BAIXAR", 
                                      command=self.start_download,
                                      bg="#1DB954", fg="white", 
                                      font=("Arial", 12, "bold"),
                                      height=2, cursor="hand2",
                                      relief=tk.FLAT, borderwidth=0)
        self.download_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        self.install_btn = tk.Button(button_frame, text="🔧 Instalar\nDependências", 
                                     command=self.install_dependencies,
                                     bg="#535353", fg="white", 
                                     font=("Arial", 9, "bold"),
                                     height=2, cursor="hand2",
                                     relief=tk.FLAT, borderwidth=0)
        self.install_btn.pack(side=tk.LEFT, padx=(5, 0))
        
        # Área de log
        log_label = ttk.Label(main_frame, text="Log de download:")
        log_label.pack(anchor=tk.W)
        
        self.log_text = scrolledtext.ScrolledText(main_frame, height=10, 
                                                   font=("Consolas", 9),
                                                   bg="#282828", fg="#FFFFFF",
                                                   insertbackground="white")
        self.log_text.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        
        # Barra de progresso
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.pack(fill=tk.X, pady=(10, 0))
        
        # Status
        self.status_label = ttk.Label(main_frame, text="Aguardando verificação...", 
                                      font=("Arial", 9), foreground="#B3B3B3")
        self.status_label.pack(pady=(5, 0))
    
    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.download_path.set(folder)
    
    def log(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()
    
    def find_spotdl(self):
        """Encontra o caminho do spotdl"""
        try:
            # Tentar encontrar spotdl usando where (Windows)
            result = subprocess.run(["where", "spotdl"], 
                                   capture_output=True, text=True)
            if result.returncode == 0:
                path = result.stdout.strip().split('\n')[0]
                return path
        except:
            pass
        
        # Tentar caminhos comuns
        possible_paths = [
            os.path.join(os.path.dirname(sys.executable), "Scripts", "spotdl.exe"),
            os.path.join(os.path.dirname(sys.executable), "spotdl.exe"),
            "spotdl"
        ]
        
        for path in possible_paths:
            try:
                result = subprocess.run([path, "--version"], 
                                       capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    return path
            except:
                continue
        
        return None
    
    def install_dependencies(self):
        """Instala ou reinstala dependências"""
        self.log("\n" + "="*60)
        self.log("📦 Instalando dependências...")
        self.log("="*60 + "\n")
        
        self.install_btn.config(state=tk.DISABLED)
        self.status_label.config(text="Instalando dependências...")
        
        def install():
            try:
                # Atualizar pip
                self.log("🔄 Atualizando pip...")
                subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
                              capture_output=True, text=True)
                
                # Instalar spotdl
                self.log("📥 Instalando spotdl...")
                result = subprocess.run([sys.executable, "-m", "pip", "install", 
                                        "--upgrade", "spotdl"],
                                       capture_output=True, text=True)
                
                if result.returncode == 0:
                    self.log("✅ spotdl instalado com sucesso!")
                    self.log("\n" + result.stdout)
                else:
                    self.log("❌ Erro ao instalar spotdl:")
                    self.log(result.stderr)
                
                # Instalar yt-dlp (backend do spotdl)
                self.log("\n📥 Instalando yt-dlp...")
                result = subprocess.run([sys.executable, "-m", "pip", "install", 
                                        "--upgrade", "yt-dlp"],
                                       capture_output=True, text=True)
                
                if result.returncode == 0:
                    self.log("✅ yt-dlp instalado com sucesso!")
                else:
                    self.log("❌ Erro ao instalar yt-dlp:")
                    self.log(result.stderr)
                
                self.log("\n" + "="*60)
                self.log("✅ Instalação concluída!")
                self.log("="*60 + "\n")
                
                # Verificar novamente
                self.check_dependencies()
                
            except Exception as e:
                self.log(f"\n❌ Erro durante instalação: {str(e)}")
            finally:
                self.install_btn.config(state=tk.NORMAL)
        
        thread = threading.Thread(target=install)
        thread.daemon = True
        thread.start()
    
    def check_dependencies(self):
        self.log("🔍 Verificando dependências...\n")
        
        # Verificar spotdl
        self.spotdl_path = self.find_spotdl()
        
        if self.spotdl_path:
            try:
                result = subprocess.run([self.spotdl_path, "--version"],
                                       capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    version = result.stdout.strip()
                    self.log(f"✅ spotdl encontrado: {version}")
                    self.log(f"📍 Caminho: {self.spotdl_path}\n")
                    self.status_label.config(text="Pronto para download")
                    self.download_btn.config(state=tk.NORMAL)
                    return
            except Exception as e:
                self.log(f"⚠️ Erro ao verificar spotdl: {str(e)}")
        
        self.log("❌ spotdl não encontrado!")
        self.log("💡 Clique em 'Instalar Dependências' para instalar\n")
        self.status_label.config(text="Dependências não instaladas")
        self.download_btn.config(state=tk.DISABLED)
    
    def start_download(self):
        url = self.url_var.get().strip()
        
        if not url:
            messagebox.showwarning("Aviso", "Por favor, insira uma URL do Spotify!")
            return
        
        if not ("spotify.com" in url):
            messagebox.showwarning("Aviso", "URL inválida! Use um link do Spotify.")
            return
        
        if self.is_downloading:
            messagebox.showinfo("Aviso", "Um download já está em andamento!")
            return
        
        if not self.spotdl_path:
            messagebox.showerror("Erro", "spotdl não está instalado!\nClique em 'Instalar Dependências'")
            return
        
        # Criar pasta de destino se não existir
        dest_path = self.download_path.get()
        os.makedirs(dest_path, exist_ok=True)
        
        # Iniciar download em thread separada
        thread = threading.Thread(target=self.download, args=(url, dest_path))
        thread.daemon = True
        thread.start()
    
    def download(self, url, dest_path):
        self.is_downloading = True
        self.download_btn.config(state=tk.DISABLED, text="⏳ BAIXANDO...")
        self.progress.start(10)
        self.status_label.config(text="Download em andamento...")
        
        self.log(f"\n{'='*60}")
        self.log(f"🎵 Iniciando download...")
        self.log(f"📍 URL: {url}")
        self.log(f"📁 Destino: {dest_path}")
        self.log(f"{'='*60}\n")
        
        try:
            # Construir comando spotdl
            format_type = self.format_var.get()
            bitrate = self.quality_var.get()
            
            cmd = [
                self.spotdl_path,
                "download",
                url,
                "--output", dest_path,
                "--format", format_type,
                "--bitrate", f"{bitrate}k"
            ]
            
            self.log(f"🔧 Comando: {' '.join(cmd)}\n")
            
            # Executar spotdl
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                encoding='utf-8',
                errors='replace'
            )
            
            # Ler output em tempo real
            for line in process.stdout:
                line = line.strip()
                if line:
                    self.log(line)
            
            process.wait()
            
            if process.returncode == 0:
                self.log(f"\n{'='*60}")
                self.log("✅ Download concluído com sucesso!")
                self.log(f"📁 Arquivos salvos em: {dest_path}")
                self.log(f"{'='*60}\n")
                self.status_label.config(text="Download concluído!")
                messagebox.showinfo("Sucesso", 
                                    f"Download concluído!\n\nArquivos salvos em:\n{dest_path}")
                
                # Abrir pasta
                os.startfile(dest_path)
            else:
                self.log(f"\n❌ Erro durante o download (código: {process.returncode})")
                self.log("💡 Possíveis causas:")
                self.log("   - URL inválida ou conteúdo indisponível")
                self.log("   - Problema de conexão com a internet")
                self.log("   - FFmpeg não instalado")
                self.status_label.config(text="Erro no download")
                messagebox.showerror("Erro", 
                    "Erro durante o download.\n\n" +
                    "Verifique:\n" +
                    "1. Se a URL está correta\n" +
                    "2. Sua conexão com internet\n" +
                    "3. Se FFmpeg está instalado")
        
        except Exception as e:
            self.log(f"\n❌ Erro: {str(e)}")
            self.status_label.config(text="Erro no download")
            messagebox.showerror("Erro", f"Erro durante o download:\n{str(e)}")
        
        finally:
            self.is_downloading = False
            self.download_btn.config(state=tk.NORMAL, text="⬇ BAIXAR")
            self.progress.stop()

def main():
    root = tk.Tk()
    app = SpotifyDownloader(root)
    root.mainloop()

if __name__ == "__main__":
    main()