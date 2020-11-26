# %%
# from fpdf import FPDF
# import img2pdf
import glob
from PIL import Image
import re


def imgs2pdf(files, outfile):
    img, *imgs = [Image.open(f) for f in sorted(files)]
    img.save(fp=outfile, format='PDF', append_images=imgs,
             save_all=True)


def imgs2gif(files, outfile, duration):
    img, *imgs = [Image.open(f) for f in sorted(files)]
    img.save(fp=outfile, format='GIF', append_images=imgs,
             save_all=True, duration=duration, loop=0)


def combine_images(indir="./synoptic/850", prefix="ESPBT_ACWP_L85",
    file_types = "pdf", duration = 1500):
    """
    - `file_types`: `pdf` or `gif`
    
    # References
    - https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
    """
    pattern = "%s/*%s*.png" % (indir, prefix)

    files = glob.glob(pattern)
    files = sorted(files)
    print(" ... %d images will be processed" % len(files))

    date_begin = re.findall(r"\d{10}", files[1])[0]
    date_end = re.findall(r"\d{10}", files[-1])[0]
    # files[1], files[len(files)-1]
    if not isinstance(file_types, list): file_types = [file_types]
    
    for file_type in file_types:
        outfile = "%s-[%s, %s].%s" % (prefix, date_begin, date_end, file_type)
        if file_type == "pdf":
            imgs2pdf(files, outfile)
        elif file_type == "gif":
            imgs2gif(files, outfile, duration = duration)

# files = glob.glob("synoptic/850")
# with open("name.pdf","wb") as f:
    # f.write(img2pdf.convert(files))

# pdf = FPDF()
# # imagelist is the list with all image filenames
# for image in files:
#     pdf.add_page()
#     pdf.image(image, x, y, w, h)
# pdf.output("yourfile.pdf", "F")


# %%
combine_images("synoptic/850", "ESPBT_ACWP_L85", file_types= ["pdf", "gif"])
combine_images("synoptic/000", "ESPBT_ACWP_L00", file_types=["pdf", "gif"])

combine_images("synoptic/850", "ESPCT_ACWP_L85", file_types=["pdf", "gif"])
combine_images("synoptic/000", "ESPCT_ACWP_L00", file_types=["pdf", "gif"])
