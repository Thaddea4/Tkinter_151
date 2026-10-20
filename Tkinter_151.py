import tkinter as tk

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("450x550")

def hasil():
    popup = tk.Toplevel(root)
    popup.title("Hasil Prediksi")
    popup.geometry("350x150")
    tk.Label(popup, text="Prediksi Prodi: Teknologi Informasi",
             font=("Arial", 12, "bold")).pack(pady=50)

root.mainloop()