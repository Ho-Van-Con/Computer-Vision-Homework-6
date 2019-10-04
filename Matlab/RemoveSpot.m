function RemoveSpot
img = imread('image.jpg');
img_gray = rgb2gray(img);
BW = imbinarize(img_gray,0.47);%if your matlab version 2016 or less to use function im2bw(img,0.47)
BW = ~BW;
dest_img = bwareaopen(BW,200);
dest_img = ~dest_img;
imshow(dest_img);
end