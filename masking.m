[im1, R] = geotiffread(['classif_map2']);
[im2, R] = geotiffread(['classification_map']);
im1 = im1(:,:,1);
im2 = im2(:,:,1);
res = zeros(size(im1,1), size(im1,2));
res(im1==1)=1;
res(im2==2 & im1==1)=2;
res(im1==3&im2~=1)=3;
geotiffwrite(['result.tif'], uint8(res), R, 'GeoKeyDirectoryTag', info.GeoTIFFTags.GeoKeyDirectoryTag);