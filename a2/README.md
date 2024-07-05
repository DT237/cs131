1. What this command does
The webptopng.sh script takes a folder with a path designated by the user, checks it for any images with the WebP file format, and converts all the images within the folder to the PNG file format. 
These converted images are then outputted to an additional folder within the desginated path to separate it from the source images.

2. Why/When this command is useful 
The WebP file format was developed by Google to replace older image file formats like PNG and JPEG but WebP images is not universally supported by all websites, notably Imgur which a popular image sharing website.
As a result, a WebP file must be converted to a more commonly used file format such as PNG which is what this script does. PNG was chosen due to its universality and because it is lossless, meaning it will 
often preserve image quality better than formats like JPEG. This script is also useful because it can mass convert WebP images in a folder just by running the script, while other methods may require the user 
to convert each image individually which is very time consuming.

3. How you can use this command
Before webptopng.sh can be run, the user must download FFMPEG which is a tool used for processing images and videos. ffmpeg_install.sh is a preliminary script included alongside webptopng.sh that can be run to 
install FFMPEG on the user's computer.
-Download ffmpeg_install.sh and webptopng.sh to your desired directory.
-Change to the directory in the terminal to the one where the scripts have been installed in. Ex: "cd /Users/devin.tran/desktop/" (Don't include quotation marks in the command)
-Create a folder anywhere you want and insert your .WEBP files.
-If you do not have FFMPEG installed, run ffmpeg_install.sh by typing the command "./ffmpeg_install.sh" into your terminal. NOTE: the current working directory must be the same as the one that includes the scripts.
-Afterwards, run webptopng.sh by typing "./webptopng.sh" into your terminal. This will prompt you to insert the path to the folder you have your WeBP files stored in.
-Type in the path to your folder. Ex: "/Users/devin.tran/desktop/pics"
-If the path is not detected, the script will exit and you may activate the script again and try to correctly input your path.
-If the path is detected. All WebP files found in the folder will be converted to PNGs and stored in a folder called "png_files" within the folder you have included your WebP files.



4. Examples (Copy/Paste the actual terminal execution results)
devin.tran@Macbook desktop % ./webptopng.sh
Please enter the path of the folder containing the .WEBP files: 
/Users/devin.tran/desktop/pics/
ffmpeg version 7.0.1 Copyright (c) 2000-2024 the FFmpeg developers
  built with Apple clang version 13.0.0 (clang-1300.0.29.30)
  configuration: --prefix=/usr/local/Cellar/ffmpeg/7.0.1 --enable-shared --enable-pthreads --enable-version3 --cc=clang --host-cflags= --host-ldflags= --enable-ffplay --enable-gnutls --enable-gpl --enable-libaom --enable-libaribb24 --enable-libbluray --enable-libdav1d --enable-libharfbuzz --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librav1e --enable-librist --enable-librubberband --enable-libsnappy --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtesseract --enable-libtheora --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libxvid --enable-lzma --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libspeex --enable-libsoxr --enable-libzmq --enable-libzimg --disable-libjack --disable-indev=jack --enable-videotoolbox --enable-audiotoolbox
  libavutil      59.  8.100 / 59.  8.100
  libavcodec     61.  3.100 / 61.  3.100
  libavformat    61.  1.100 / 61.  1.100
  libavdevice    61.  1.100 / 61.  1.100
  libavfilter    10.  1.100 / 10.  1.100
  libswscale      8.  1.100 /  8.  1.100
  libswresample   5.  1.100 /  5.  1.100
  libpostproc    58.  1.100 / 58.  1.100
Input #0, webp_pipe, from '/Users/devin.tran/desktop/pics//1.sm.webp':
  Duration: N/A, bitrate: N/A
  Stream #0:0: Video: webp, yuv420p(tv, bt470bg/unknown/unknown), 320x214, 25 fps, 25 tbr, 25 tbn
Stream mapping:
  Stream #0:0 -> #0:0 (webp (native) -> png (native))
Press [q] to stop, [?] for help
Output #0, image2, to '/Users/devin.tran/desktop/pics//png_files/1.sm.webp.png':
  Metadata:
    encoder         : Lavf61.1.100
  Stream #0:0: Video: png, rgb24(pc, gbr/unknown/unknown, progressive), 320x214, q=2-31, 200 kb/s, 25 fps, 25 tbn
      Metadata:
        encoder         : Lavc61.3.100 png
[image2 @ 0x7fa0f8e0e380] The specified filename '/Users/devin.tran/desktop/pics//png_files/1.sm.webp.png' does not contain an image sequence pattern or a pattern is invalid.
[image2 @ 0x7fa0f8e0e380] Use a pattern such as %03d for an image sequence or use the -update option (with -frames:v 1 if needed) to write a single image.
[out#0/image2 @ 0x7fa0f8e09a80] video:104KiB audio:0KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown
frame=    1 fps=0.0 q=-0.0 Lsize=N/A time=00:00:00.04 bitrate=N/A speed=4.01x    
ffmpeg version 7.0.1 Copyright (c) 2000-2024 the FFmpeg developers
  built with Apple clang version 13.0.0 (clang-1300.0.29.30)
  configuration: --prefix=/usr/local/Cellar/ffmpeg/7.0.1 --enable-shared --enable-pthreads --enable-version3 --cc=clang --host-cflags= --host-ldflags= --enable-ffplay --enable-gnutls --enable-gpl --enable-libaom --enable-libaribb24 --enable-libbluray --enable-libdav1d --enable-libharfbuzz --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librav1e --enable-librist --enable-librubberband --enable-libsnappy --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtesseract --enable-libtheora --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libxvid --enable-lzma --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libspeex --enable-libsoxr --enable-libzmq --enable-libzimg --disable-libjack --disable-indev=jack --enable-videotoolbox --enable-audiotoolbox
  libavutil      59.  8.100 / 59.  8.100
  libavcodec     61.  3.100 / 61.  3.100
  libavformat    61.  1.100 / 61.  1.100
  libavdevice    61.  1.100 / 61.  1.100
  libavfilter    10.  1.100 / 10.  1.100
  libswscale      8.  1.100 /  8.  1.100
  libswresample   5.  1.100 /  5.  1.100
  libpostproc    58.  1.100 / 58.  1.100
Input #0, webp_pipe, from '/Users/devin.tran/desktop/pics//2.sm.webp':
  Duration: N/A, bitrate: N/A
  Stream #0:0: Video: webp, yuv420p(tv, bt470bg/unknown/unknown), 320x235, 25 fps, 25 tbr, 25 tbn
Stream mapping:
  Stream #0:0 -> #0:0 (webp (native) -> png (native))
Press [q] to stop, [?] for help
Output #0, image2, to '/Users/devin.tran/desktop/pics//png_files/2.sm.webp.png':
  Metadata:
    encoder         : Lavf61.1.100
  Stream #0:0: Video: png, rgb24(pc, gbr/unknown/unknown, progressive), 320x235, q=2-31, 200 kb/s, 25 fps, 25 tbn
      Metadata:
        encoder         : Lavc61.3.100 png
[image2 @ 0x7fd0de60cc00] The specified filename '/Users/devin.tran/desktop/pics//png_files/2.sm.webp.png' does not contain an image sequence pattern or a pattern is invalid.
[image2 @ 0x7fd0de60cc00] Use a pattern such as %03d for an image sequence or use the -update option (with -frames:v 1 if needed) to write a single image.
[out#0/image2 @ 0x7fd0de60c0c0] video:165KiB audio:0KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown
frame=    1 fps=0.0 q=-0.0 Lsize=N/A time=00:00:00.04 bitrate=N/A speed=2.71x    
.WEBP to .PNG conversion complete. .PNG files are stored in /Users/devin.tran/desktop/pics//png_files.
