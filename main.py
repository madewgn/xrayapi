

import subprocess



def vmess(u,exp):


# Menjalankan perintah "add-ws" dengan subprocess
    process = subprocess.Popen(["/bin/add-ws"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    # Mengambil input dari pengguna
    username = u
    hari = exp

    # Mengirim input ke perintah "add-ws"
    input_text = f"{username}\n{hari}\n"
    output, errors = process.communicate(input=input_text)

    # Menampilkan output
    print(output)

# Menampilkan pesan kesalahan jika ada
    if errors:
        print("Error:", errors)
if __name__ == "__main__":
    vmess("ydzyyd","1")
