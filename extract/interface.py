import os
import extract as e


def analysis(path):
    file_path = os.path.abspath(__file__)
    file_dir = os.path.dirname(file_path)
    test_path = os.path.join(file_dir, "../test.py")
    os.system("python -u " + test_path +"\
        --imgs %s  \
        --cfg ../config/ade20k-resnet101-upernet.yaml \
        TEST.result ./ \
        TEST.suffix _epoch_40.pth" % (path))


def analysis_for_video(path):
    result_path = os.path.join(os.path.dirname(path), "images")
    # print("result_path=" + result_path)
    # print("==============================================================")
    # print("**         choose the way you want to analyse video         **")
    # print("**              1-  the information of the video            **")
    # print("**       2-  input the pointer of the video yourself        **")
    # print("**        3-  extract images with continuous manner         **")
    # print("**          4-  extract images at custom intervals          **")
    # print("==============================================================")
    # print("please choose: ")
    _str = input()
    switch_case(_str, path, result_path)
    analysis(result_path)


# 该函数拆分为了两个，原函数用来得出视频信息，拆出来的函数用来调用第二组工作
def switch_case(choose, path, result_path):
    time_list = []
    if choose == "1":
        video_infor = e.ExtractPictures.video_frames(
            path_in=path,
            path_out=result_path,
            only_output_video_info=True,
            extract_time_points=None,
            initial_extract_time=0,
            end_extract_time=None,
            extract_time_interval=-1,
            output_prefix='extract',
            jpg_quality=100,
        )
        return video_infor

    if choose == "2":
        print("please input the pointers you like: ")
        list_ = list(map(float, input().strip().split()))
        time_list = e.ExtractPictures.video_frames(
            path_in=path,
            path_out=result_path,
            only_output_video_info=False,
            extract_time_points=list_,
            initial_extract_time=0,
            end_extract_time=None,
            extract_time_interval=-1,
            output_prefix='extract',
            jpg_quality=100,
        )
    if choose == "3":
        print("do you want to input the start time and the finish time you like?(yes or no)")
        str_ = input()
        if str_ == "yes":
            print("start_time: ")
            start_time = float(input())
            print("end_time: ")
            end_time = float(input())
            time_list = e.ExtractPictures.video_frames(
                path_in=path,
                path_out=result_path,
                only_output_video_info=False,
                extract_time_points=None,
                initial_extract_time=start_time,
                end_extract_time=end_time,
                extract_time_interval=-1,
                output_prefix='extract',
                jpg_quality=100,
            )
        else:
            print("extracting pictures, please wait........")
            time_list = e.ExtractPictures.video_frames(
                path_in=path,
                path_out=result_path,
                only_output_video_info=False,
                extract_time_points=None,
                initial_extract_time=0,
                end_extract_time=None,
                extract_time_interval=-1,
                output_prefix='extract',
                jpg_quality=100,
            )
    # if choose == "4":
    #     print("do you want to output the start time and the finish time you like?(yes or no)")
    #     str_ = input()
    #     if str_ == "yes":
    #         print("start_time (s): ")
    #         start_time = float(input())
    #         print("end_time (s): ")
    #         end_time = float(input())
    #         print("Please input the interval you like, (s): ")
    #         interval = float(input())
    #         time_list = e.ExtractPictures.video_frames(
    #             path_in=path,
    #             path_out=result_path,
    #             only_output_video_info=False,
    #             extract_time_points=None,
    #             initial_extract_time=start_time,
    #             end_extract_time=end_time,
    #             extract_time_interval=interval,
    #             output_prefix='extract',
    #             jpg_quality=100,
    #         )
    #     else:
    #         print("Please input the interval you like, (s): ")
    #         interval = float(input())
    #         time_list = e.ExtractPictures.video_frames(
    #             path_in=path,
    #             path_out=result_path,
    #             only_output_video_info=False,
    #             extract_time_points=None,
    #             initial_extract_time=0,
    #             end_extract_time=None,
    #             extract_time_interval=interval,
    #             output_prefix='extract',
    #             jpg_quality=100,
    #         )
    # print("This is time_list:")
    # print(time_list)


# 用来向后端传递用户输入
def pass_input(start_time, end_time, interval, path, result_path):
    time_list = e.ExtractPictures.video_frames(
                path_in=path,
                path_out=result_path,
                only_output_video_info=False,
                extract_time_points=None,
                initial_extract_time=start_time,
                end_extract_time=end_time,
                extract_time_interval=interval,
                output_prefix='extract',
                jpg_quality=100,
            )

    return time_list

#
# if __name__ == '__main__':
#     analysis_for_video("/Users/apple/Documents/GitHub/Visual-fixation-system/output/test.mp4")
