import os
import cv2
import argparse
import glob

def parse_arguments():
    parser = argparse.ArgumentParser(description='prepare data')
    parser.add_argument('--input','-i', type=str, nargs='+', help='path to the video')
    parser.add_argument('--target','-t', type=str, default='', help='target output')
    parser.add_argument('--frame', '-f', type=int, default=10, help='the frame speed we will parse the video')
    args = parser.parser_args()
    return args

def parse_video(video, output, frame):
    times = 0
    if not os.path.exists(output):
        os.makedirs(output)
    camera = cv2.VideoCapture(video)
    i = 0
    while True:
        times += 1
        res, image = camera.read()
        if not res:
            break
        if times % frame == 0:
            cv2.imwrite(output + outputstring(i) + '.jpg', image)
            print(output + outputstring(i) + '.jpg')
            i+=1
    print("Finished")

def outputstring(num):
    if num < 10:
        return "0" * 4 + str(num)
    elif num < 100:
        return "0" * 3 + str(num)
    elif num < 1000:
        return "0" * 2 + str(num)
    elif num < 10000:
        return "0" + str(num)
    else:
        return str(num)

def main():
    args = parse_arguments()
    print("input file: " + args.input)
    print("output directory: " + args.target)
    print("frame speed: " + args.frame)
    parse_video(args.input, args.target, args.frame)

if __name__ == "main":
    main()
