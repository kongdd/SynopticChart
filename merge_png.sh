
# rm out.mp4
# 
# ffmpeg -f image2 -framerate 1 -i SEVP_NMC_WESA_SFER_EGH_ACWP_L00_P9_%017d.png \
#     -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4

rm test.avi
ffmpeg -c:v mjpeg -framerate 1 -r 1 -f image2 -pattern_type glob -i "*.png" -pix_fmt yuv420p -qscale 1 test.avi
# ffmpeg -c:v mjpeg -framerate 1 -r 1 -f image2 -i %1d.png test.avi

# ffmpeg -f image2 -framerates 1 -i 1.png \
#     -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4
# ffmpeg -f image2 -framerate 1 -i 1.png -i 2.png \
#     -c:v libx264 -r 30 -vcodec mjpeg out.mp4
# -pix_fmt yuv420p
# ffmpeg -r 1 -i %01d.png -vcodec mpeg4 -y movie.mp4
