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

tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan",
         font=("Arial", 16, "bold")).pack(pady=20)

frame = tk.Frame(root)
frame.pack()

for i in range(1, 11):
    tk.Label(frame, text=f"Nilai Mata Pelajaran {i}:").grid(
        row=i, column=0, pady=5)
    tk.Entry(frame, width=20).grid(row=i, column=1, padx=10)
    
    tk.Label(root, text="Pilihan Jurusan Anda:").pack(pady=10)
    
root.mainloop()