import cv2
import os


def create_video_from_images(image_folder, output_video, fps=30):
    # Récupérer les fichiers d'images
    images = [img for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))]
    images.sort()  # Trier les images par nom de fichier
    

    if not images:
        raise ValueError("Aucune image trouvée dans le dossier spécifié.")

    # Lire la première image pour obtenir les dimensions
    first_image_path = os.path.join(image_folder, images[0])
    frame = cv2.imread(first_image_path)
    height, width, layers = frame.shape

    # Initialiser le writer vidéo
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec vidéo pour mp4
    video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    for image in images:
        image_path = os.path.join(image_folder, image)
        frame = cv2.imread(image_path)
        video.write(frame)

    # Libérer le writer vidéo
    video.release()
    print(f"Vidéo créée : {output_video}")

# Exemple d'utilisation
image_folder = 'result'  # Remplacer par le chemin de votre dossier d'images
output_video = 'result.mp4'  # Nom de la vidéo de sortie

create_video_from_images(image_folder, output_video, fps=5)
