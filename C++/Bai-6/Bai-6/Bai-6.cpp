// Bai-6.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

using namespace cv;
using namespace std;

int main()
{
	Mat OriginalImage, OriginalImageResize;
	Mat GrayImage;
	Mat BinnaryImageToZero, BinaryImage;
	Mat DestinationImage;
	const char* title_original_image = "Original Image";
	OriginalImage = imread("..\\image.jpg");
	resize(OriginalImage, OriginalImageResize,cv::Size((OriginalImage.cols / 3),(OriginalImage.rows / 3)));
	namedWindow(title_original_image, WINDOW_AUTOSIZE);
	cvtColor(OriginalImageResize, GrayImage, COLOR_RGB2GRAY);
	threshold(GrayImage, BinnaryImageToZero, 0, 255, THRESH_TOZERO);
	threshold(GrayImage, BinaryImage, 120, 255, THRESH_BINARY);
	Mat element = getStructuringElement(MORPH_RECT, cv::Size(5, 5), Point(-1, -1));
	dilate(BinnaryImageToZero, DestinationImage, element, Point(-1, -1));
	erode(DestinationImage, DestinationImage, element, Point(-1, -1));
	imshow(title_original_image, OriginalImageResize);
	imshow("Binary Image", BinaryImage);
	imshow("Destion Image", DestinationImage);
	waitKey(0);
	destroyAllWindows();
	return 0;
}