import os
import moviepy.editor as mp



folder_path = '.\\DRAFT\\Videos_Local'     
# Procurando todos os diretorios
for file_name in os.listdir(folder_path):
    # Procurando os videos mp4
    if file_name.endswith('.mp4'):
        mp4_file = folder_path+r'\\'+file_name
        videoclip = mp.VideoFileClip(mp4_file)
        videoclip.write_videofile( folder_path+r'\\'+os.path.splitext(file_name)[0]+r'.webm',codec='libvpx-vp9',
                bitrate='525k',
                ffmpeg_params=[
                    '-tile-columns', '6', '-frame-parallel', '0',
                    '-auto-alt-ref', '1', '-lag-in-frames', '25', '-g',
                    '128', '-pix_fmt', 'yuv420p', '-row-mt', '1'])

