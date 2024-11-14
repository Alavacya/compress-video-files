import os
from moviepy.editor import VideoFileClip

fnames = input('Введите имена файлов с расширением (разделите пробелом): ')

file_list = fnames.split()

output_format = input('Введите формат сохранения (.mp4 или .webm): ').lower()

if output_format not in ['.mp4', '.webm']:
	print('Неподдерживаемый формат сохранения. Программа завершена.')
	exit()

for fname in file_list:
	if not os.path.exists(fname):
		print(f'Файл {fname} не существует.')
	else:
		clip = VideoFileClip(fname)

		filename, _ = os.path.splitext(fname)

		output_compressed = f'{filename}_compressed{output_format}'

		if output_format == '.mp4':
			clip.write_videofile(output_compressed, codec='libx264', audio_codec='aac', preset='medium', threads=4, fps=clip.fps, bitrate='2000k')
		elif output_format == '.webm':
			clip.write_videofile(output_compressed, codec='libvpx-vp9', audio_codec='libvorbis', preset='medium', threads=4, fps=clip.fps, bitrate='2000k')

		print(f'Сжатие для файла {fname} завершено. Результат сохранен в {os.path.abspath(output_compressed)}')

print('Скрипт выполнен успешно.')
