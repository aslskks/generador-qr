import qrcode
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def main():
    def generate_qr():
        data_type = data_type_var.get()
        data = data_entry.get()
        filename = filename_entry.get()
    
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
    
        img = qr.make_image(fill_color="black", back_color="white")
        img_filename = f'{filename}_qrcode.png'
        img.save(img_filename)
    
        img = Image.open(img_filename)
        img.thumbnail((300, 300))
        img = ImageTk.PhotoImage(img)
        qr_label.config(image=img)
        qr_label.image = img
    
    
    # Crear la ventana de la aplicación
    app = tk.Tk()
    app.title("Generador de Códigos QR")
    
    data_type_var = tk.StringVar(value="url")
    
    data_label = tk.Label(app, text="Datos:")
    data_label.pack()
    
    data_entry = tk.Entry(app)
    data_entry.pack()
    
    filename_label = tk.Label(app, text="Nombre del archivo:")
    filename_label.pack()
    
    filename_entry = tk.Entry(app)
    filename_entry.pack()
    
    data_type_radio_url = tk.Radiobutton(
        app, text="URL", variable=data_type_var, value="url")
    data_type_radio_url.pack()
    
    data_type_radio_text = tk.Radiobutton(
        app, text="Texto", variable=data_type_var, value="text")
    data_type_radio_text.pack()
    
    generate_button = tk.Button(app, text="Generar QR", command=generate_qr)
    generate_button.pack()
    
    qr_label = tk.Label(app)
    qr_label.pack()
    
    app.mainloop()
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        import sys
        sys.exit()
    except Exception as e:
        from tkinter import messagebox
        messagebox.showerror(title="titulo", message=f"{e}")
