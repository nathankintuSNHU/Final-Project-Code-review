import tkinter.messagebox as mb
import os
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
import ctypes
import matplotlib.pyplot as plt
import numpy as np
import statistics
from PIL import Image, ImageTk

# Improve Screen DPI
ctypes.windll.shcore.SetProcessDpiAwareness(2)

# ---------------------Login page----------------------------
window = ttk.Window()
window.geometry("405x523")
window.title('Predictor')
window.iconbitmap('desktop_icon.ico')
window.tk.call("tk", "scaling", 1.33)

style = Style(theme='lumen')
window = style.master

window_frame = ttk.Frame(window)
window_frame.place(relx=0.5, rely=0.5, width=405, height=523, anchor='center')

# Create Tab Control
tab_control = ttk.Notebook(window_frame)
tab_control.place(x=0, y=0)

# Tab0
frame_one_nb = ttk.Frame(tab_control)
tab_control.add(frame_one_nb, text='Predictor')
tab_control.pack(expand=1, pady=0, fill="both")

log_img = Image.open("headingLaser.png")
photo = ImageTk.PhotoImage(log_img)
lg_label = ttk.Label(frame_one_nb, image=photo)
lg_label.place(x=0, y=0)

laser_frame = ttk.LabelFrame(frame_one_nb, text="Laser Cutting Parameters", width=190, height=365, )
laser_frame.place(x=15, y=110)

result_frame = ttk.LabelFrame(frame_one_nb, text="Results", width=165, height=365, )
result_frame.place(x=220, y=110)

pulse_width_label = ttk.Label(result_frame, text='Pulse Width(ms)', font=('calibri', 15, 'bold'))
pulse_width_label.place(x=15, y=60)

pulse_width_answer = ttk.Label(result_frame, text='----------', font=('calibri light', 18))
pulse_width_answer.place(x=15, y=90)

frequency_label = ttk.Label(result_frame, text='Frequency(Hz)', font=('calibri', 15, 'bold'))
frequency_label.place(x=15, y=140)

frequency_answer = ttk.Label(result_frame, text='----------', font=('calibri light', 18))
frequency_answer.place(x=15, y=170)

speed_label = ttk.Label(result_frame, text='Speed(mm/s)', font=('calibri', 15, 'bold'))
speed_label.place(x=15, y=220)

speed_answer = ttk.Label(result_frame, text='----------', font=('calibri light', 18))
speed_answer.place(x=15, y=250)


def setup_laser():
    setup_laser_win = tk.Toplevel()
    setup_laser_win.title("Laser Setup")
    # setup_laser_win.iconbitmap('desktop_icon.ico.')
    setup_laser_win_width = 590
    setup_laser_win_height = 120
    setup_laser_win_screen_width = setup_laser_win.winfo_screenwidth()
    setup_laser_win_screen_height = setup_laser_win.winfo_screenheight()
    x_setup_laser_win = (setup_laser_win_screen_width / 2) - (setup_laser_win_width / 2)
    y_setup_laser_win = (setup_laser_win_screen_height / 2) - (setup_laser_win_height / 2)
    setup_laser_win.geometry(
        "%dx%d+%d+%d" % (setup_laser_win_width, setup_laser_win_height, x_setup_laser_win, y_setup_laser_win))
    setup_laser_win.resizable(False, False)

    def laser_save():
        select_laser = laserPowerSetup.get()
        if select_laser == laserOne:
            with open('laser_directory\\laserOne.txt', "w") as file_one:
                file_link = str(laserSet_upEntry.get())
                file_one.write(file_link)
                file_one.close()
                with open('laser_directory\\laserOneName.txt', "w") as file_one_name:
                    laserFolderName = str(laserEntry_name.get())
                    file_one_name.write(laserFolderName)
                    file_one_name.close()
                mb.showinfo(title="Laser Name", message='Laser one has successfully saved')
            setup_laser_win.destroy()

        elif select_laser == laserTwo:
            with open('laser_directory\\laserTwo.txt', "w") as file_two:
                file_link = str(laserSet_upEntry.get())
                file_two.write(file_link)
                file_two.close()
                with open('laser_directory\\laserTwoName.txt', "w") as file_two_name:
                    laserFolderName = str(laserEntry_name.get())
                    file_two_name.write(laserFolderName)
                    file_two_name.close()
                mb.showinfo(title="Save Storage Link", message='Storage Two has successfully saved')
            setup_laser_win.destroy()

        elif select_laser == laserThree:
            with open('laser_directory\\laserThree.txt', "w") as file_three:
                file_link = str(laserSet_upEntry.get())
                file_three.write(file_link)
                file_three.close()
                with open('laser_directory\\laserThreeName.txt', "w") as file_three_name:
                    laserFolderName = str(laserEntry_name.get())
                    file_three_name.write(laserFolderName)
                    file_three_name.close()
                mb.showinfo(title="Save Storage Link", message='Storage Three has successfully saved')
            setup_laser_win.destroy()

        elif select_laser == laserFour:
            with open('laser_directory\\laserFour.txt', "w") as file_four:
                file_link = str(laserSet_upEntry.get())
                file_four.write(file_link)
                file_four.close()
                with open('laser_directory\\laserFourName.txt', "w") as file_four_name:
                    laserFolderName = str(laserEntry_name.get())
                    file_four_name.write(laserFolderName)
                    file_four_name.close()
                mb.showinfo(title="Save Storage Link", message='Storage Four has successfully saved')
            setup_laser_win.destroy()

        elif select_laser == laserFive:
            with open('laser_directory\\laserFive.txt', "w") as file_five:
                file_link = str(laserSet_upEntry.get())
                file_five.write(file_link)
                file_five.close()
                with open('laser_directory\\laserFiveName.txt', "w") as file_five_name:
                    laserFolderName = str(laserEntry_name.get())
                    file_five_name.write(laserFolderName)
                    file_five_name.close()
                mb.showinfo(title="Save Storage Link", message='Storage Five has successfully saved')
            setup_laser_win.destroy()

        else:
            mb.showinfo(title="Save Laser", message='Please select laser number')

    def dropdown_opened():
        mb.showinfo(title="Save", message='Please restart application after setup')

    laserPowerSetup = ttk.Combobox(setup_laser_win, values=[laserOne, laserTwo, laserThree, laserFour, laserFive],
                                   postcommand=dropdown_opened)
    laserPowerSetup.place(x=20, y=15, height=25)
    laserPowerSetup.set('Select Laser')

    laserEntry_name = ttk.Entry(setup_laser_win)
    laserEntry_name.place(x=175, y=15, width=395, height=25)
    laserEntry_name.insert(0, 'Insert Laser Watts')

    laserSet_upEntry = ttk.Entry(setup_laser_win)
    laserSet_upEntry.place(x=20, y=50, width=550, height=25)
    laserSet_upEntry.insert(0, 'Insert Laser Name')

    btn_save_storage = ttk.Button(setup_laser_win, text="Save", style='info.link', command=laser_save)
    btn_save_storage.place(x=450, y=80)


laserOne = open('laser_directory\\laserOne.txt', 'r').readline()
laserTwo = open('laser_directory\\laserTwo.txt', 'r').readline()
laserThree = open('laser_directory\\laserThree.txt', 'r').readline()
laserFour = open('laser_directory\\laserFour.txt', 'r').readline()
laserFive = open('laser_directory\\laserFive.txt', 'r').readline()


def laser_storage(event):
    laserFetch = laserPower_Entry.get()
    if laserFetch == laserOne:
        laser_path_one = open('laser_directory\\laserOneName.txt', 'r').readline()
        wattsDetails_Entry.delete(0, "end")
        wattsDetails_Entry.insert(0, laser_path_one)

    elif laserFetch == laserTwo:
        laser_path_two = open('laser_directory\\laserTwoName.txt', 'r').readline()
        wattsDetails_Entry.delete(0, "end")
        wattsDetails_Entry.insert(0, laser_path_two)

    elif laserFetch == laserThree:
        laser_path_three = open('laser_directory\\laserThreeName.txt', 'r').readline()
        wattsDetails_Entry.delete(0, "end")
        wattsDetails_Entry.insert(0, laser_path_three)

    elif laserFetch == laserFour:
        laser_path_four = open('laser_directory\\laserFourName.txt', 'r').readline()
        wattsDetails_Entry.delete(0, "end")
        wattsDetails_Entry.insert(0, laser_path_four)

    elif laserFetch == laserFive:
        laser_path_five = open('laser_directory\\laserFiveName.txt', 'r').readline()
        wattsDetails_Entry.delete(0, "end")
        wattsDetails_Entry.insert(0, laser_path_five)

    else:
        mb.showinfo('info', 'Please select preferred Laser')


totalLengthOutput = ttk.Button(laser_frame, text='Setup Laser Profile', command=setup_laser)
totalLengthOutput.place(x=15, y=15, height=30, width=134)

design_parameter_btn = ttk.Button(laser_frame, text='Graph', command="dataEng")
design_parameter_btn.place(x=15, y=300, height=30, width=100)

freq2 = tk.StringVar()
laserPower_Entry = ttk.Combobox(laser_frame, textvariable=freq2)
laserPower_Entry["values"] = [laserOne, laserTwo, laserThree, laserFour, laserFive]
laserPower_Entry['state'] = 'readonly'
laserPower_Entry.bind("<<ComboboxSelected>>", laser_storage)
laserPower_Entry.place(x=15, y=65, height=25, width=100)
laserPower_Entry.set("Select Laser")

laserNameLabel = ttk.Label(laser_frame, text='Laser', font=('calibri', 9, 'bold'))
laserNameLabel.place(x=120, y=63)

wattsDetails_Entry = ttk.Entry(laser_frame)
wattsDetails_Entry.place(x=15, y=110, height=25, width=100)
wattsDetails_Entry.insert(0, '0.00')
wattsLabel = ttk.Label(laser_frame, text='Watts', font=('calibri', 9, 'bold'))
wattsLabel.place(x=120, y=113)

pulsePower = ttk.Label(laser_frame, text='Pulse\nPower(%)', font=('calibri', 9, 'bold'))
pulsePower.place(x=120, y=158)
pulsePower_Entry = ttk.Entry(laser_frame)
pulsePower_Entry.place(x=15, y=160, height=25, width=100)
pulsePower_Entry.insert(0, '0.00')

kerfSize = ttk.Label(laser_frame, text='Kerf Size', font=('calibri', 9, 'bold'))
kerfSize.place(x=120, y=213)
kerfSize_Entry = ttk.Entry(laser_frame)
kerfSize_Entry.place(x=15, y=210, height=25, width=100)
kerfSize_Entry.insert(0, '0.00')

wallThickDesign = ttk.Label(frame_one_nb, text='Wall Thickness', style="sandstone", font=('calibri', 14, 'bold'))
wallThickDesign.place(x=225, y=65)
wallThicknessDesign = ttk.Entry(frame_one_nb, style="info", width=25)
wallThicknessDesign.place(x=55, y=65, height=30)

laserPow = float(wattsDetails_Entry.get())

las1 = float(os.path.exists(open('laser_directory\\laserOneName.txt', 'r').readline()))
las2 = float(os.path.exists(open('laser_directory\\laserTwoName.txt', 'r').readline()))
las3 = float(os.path.exists(open('laser_directory\\laserThreeName.txt', 'r').readline()))
las4 = float(os.path.exists(open('laser_directory\\laserFourName.txt', 'r').readline()))
las5 = float(os.path.exists(open('laser_directory\\laserFiveName.txt', 'r').readline()))


def parameters():
    # Laser input fetch
    wall_thickness = wallThicknessDesign.get()
    wall_thickness = float(wall_thickness)

    # Frequency models
    freq_one = 4620 + (27890 * wall_thickness)
    freq_two = 3378 + (24632 * wall_thickness)
    freq_three = 1.0
    freq_four = 1.0
    freq_five = 1.0

    # Linear equation to predict Speed
    speed = 5.205 + (18.37 * wall_thickness)
    # speed = (round(speed))

    mainModel = open('model\\model-model.txt')
    modelRead = mainModel.readlines()
    posOne = float(modelRead[0])
    posTwo = float(modelRead[1])
    posThree = float(modelRead[2])
    pulsewidth_main_model = (posOne + ((posTwo * wall_thickness) - (posThree * (wall_thickness ** 2))))

    # Variable for predicted value
    predicted_model_var = pulsewidth_main_model

    pulse_power_percent = float(pulsePower_Entry.get())

    # laserFrequency = float(laserFreq_Entry.get())
    kerfSiz = float(kerfSize_Entry.get())

    # ____________________________________modelCalc Start______________________________________

    # Creates data set from minimum to maximum for the pulse width range
    predicted_dataset = []
    for i in range(50):
        # generating a random number in the range 1 to 50
        random_gen = np.random.uniform(low=0.000, high=0.050)
        y_value = (np.round(random_gen, 3))
        # checking whether the generated random number is not in the randomList
        if random_gen not in predicted_dataset:
            # appending the random number to the resultant list, if the condition is true
            predicted_dataset.append(y_value)

        predicted_dataset.sort()

        # assign list
        dataset = predicted_dataset
        # open file
        with open('model\\modelData.txt', 'w+') as datafile:
            # write elements of list
            for items in dataset:
                datafile.write('%s\n' % items)
        # close the file
        datafile.close()

    # mean for the predicted pulsewidth dataset
    predicted_mean = statistics.mean(predicted_dataset)

    # Data from the prediction model provided by user turned into a list
    predictModel = [predicted_model_var]

    # mean for the predicted pulsewidth dataset turned into a list
    predictModel2 = [predicted_mean]

    # Combines predicted model and mean model from dataset into one list
    predictModel.extend(predictModel2)

    # arranges list from small to large
    predictModel.sort()

    # Sets the range to create data to rerun and generate a new mean
    startData = predictModel[0]
    endData = predictModel[1]

    refineDataset = []
    for i in range(50):
        # generating a random number in the range 1 to 50
        rangeDataset = np.random.uniform(low=startData, high=endData)
        y_two = (np.round(rangeDataset, 3))
        # checking whether the generated random number is not in the randomList
        if rangeDataset not in refineDataset:
            # appending the random number to the resultant list, if the condition is true
            refineDataset.append(y_two)
        refineDataset.sort()

        # assign list
        dataset2 = refineDataset
        # open file
        with open('model\\modelData2.txt', 'w+') as data_file2:
            # write elements of list
            for items in dataset2:
                data_file2.write('%s\n' % items)
        # close the file
        data_file2.close()

    # statistics.mean(predictModel)
    predict_model_mean2 = statistics.mean(refineDataset)

    # ___________________________________ modelCalc End ___________________________________

    # __________________________________ generatedata Start _______________________________
    data1 = []
    with open('model\\modelData.txt') as f:
        for line in f.readlines():
            data1.append(float(line))

    data2 = []
    with open('model\\modelData2.txt') as f:
        for line in f.readlines():
            data2.append(float(line))

    # Using np.linspace() with num parameter
    x_value = [x_value / 1000 for x_value in range(0, 50)]
    y_value = [x_value / 1000 for x_value in range(0, 50)]

    # x = np.random.normal(0.2, 0.1, 20)
    # plot_colors = [x_value / 1 for x_value in range(0, 50)]

    def data_eng():
        plt.scatter(x_value, data1, s=10, c='teal')
        plt.plot(x_value, data2)
        # Add correlation line

        plt.title("Pulse Width Prediction")
        axes = plt.gca()
        m, b = np.polyfit(x_value, data1, 1)
        X_plot = np.linspace(axes.get_xlim()[0], axes.get_xlim()[1], 100)
        plt.plot(X_plot, m * X_plot + b, '-')
        plt.xlabel('Wall Thickness(x)')
        plt.ylabel('Pulse Width(y_value)')
        plt.grid(alpha=.6, color='green', linestyle='--', linewidth=0.5)
        plt.show()

        # Mean of the predicting data

    meanData = statistics.mean(data1)
    # Standard deviation of the predicting data
    standard_dev = round(np.std(data1), 3)
    # Confidence interval of the predicting data
    # confidenceI = interv

    design_para_btn = ttk.Button(laser_frame, text='Graph', command=data_eng)
    design_para_btn.place(x=15, y=300, height=30, width=100)

    # ___________________________________ generatedata End ________________________________

    # LASER CUTTING EQUATIONS

    laser_mod_one = float(freq_one)
    laser_mod_two = float(freq_two)
    laser_mod_three = float(freq_three)
    laser_mod_four = float(freq_four)
    laser_mod_five = float(freq_five)

    laserFrequency = 1
    pulseWidthSpi = round(predict_model_mean2, 3)
    laser_speed2 = round(speed, 2)

    if las1 == laserPow:
        laserFrequency = laser_mod_one
    elif las2 == laserPow:
        laserFrequency = laser_mod_two
    elif las3 == laserPow:
        laserFrequency = laser_mod_three
    elif las4 == laserPow:
        laserFrequency = laser_mod_four
    elif las5 == laserPow:
        laserFrequency = laser_mod_five
    else:
        mb.showinfo(title="Laser Power", message='Please Select Laser Power')

    laserPow1 = wattsDetails_Entry.get()
    laserPow2 = float(laserPow1)

    pulseWidthSpi = float(pulseWidthSpi)
    actualPulsePower = float((laserPow2 * pulse_power_percent) / 100)
    pulseEnergy = float(pulseWidthSpi * actualPulsePower)
    repRateTime1 = float(1 / laserFrequency)
    repRateTime = round(repRateTime1, 5)
    repRate1 = float(repRateTime * 1000)
    repRate = round(repRate1, 5)
    outputPower1 = float((pulseEnergy * laserFrequency) / 1000)
    outputPower = round(outputPower1, 3)
    dutyCycle1 = float(pulseWidthSpi / repRate)
    dutyCycle = round(dutyCycle1 * 100, 2)
    spotSizeOverlap1 = float(1 - (laser_speed2 / (kerfSiz * laserFrequency)))
    spotSizeOverlap = round(spotSizeOverlap1 * 100, 2)
    newMaterialBite1 = float(laser_speed2 / (kerfSiz * laserFrequency))
    newMaterialBite = round(newMaterialBite1 * 100, 2)

    parameter_display = (
            " Wall Thickness" + '\t\t\t' + str(wall_thickness) +
            "\n Pulse Width (ms)" + '\t\t' + str(pulseWidthSpi) +
            "\n Pulse Power (%)" + '\t\t' + str(pulse_power_percent) +
            "\n Laser Power (Watts)" + '\t\t' + str(laserPow1) +
            "\n Kerf Size)" + '\t\t\t' + str(kerfSiz) +
            "\n Pulse Power (Watts)" + '\t\t' + str(actualPulsePower) +
            "\n Pulse Frequency (Hz)" + '\t\t' + str(laserFrequency) +
            "\n Speed(mm/s)" + '\t\t\t' + str(laser_speed2) +
            "\n Pulse Energy (mJ)" + '\t\t' + str(pulseEnergy) +
            "\n Rep Rate Time (s)" + '\t\t' + str(repRateTime) +
            "\n Rep Rate (ms)" + '\t\t\t' + str(repRate) +
            "\n Output Power(mJ/s)" + '\t\t' + str(outputPower) +
            "\n Duty Cycle (%)" + '\t\t\t' + str(dutyCycle) +
            "\n Spot Size Overlap (%)" + '\t\t' + str(spotSizeOverlap) +
            "\n Material Bite (%)" + '\t\t' + str(newMaterialBite) +
            "\n _____________________________" +
            "\n Generated Data Mean" + '\t\t' + str(meanData) +
            "\n Standard Deviation" + '\t\t' + str(standard_dev))

    pulse_width_answer.config(text=pulseWidthSpi, font=('calibri light', 18))
    frequency_answer.config(text=laserFrequency, font=('calibri light', 18))
    speed_answer.config(text=laser_speed2, font=('calibri light', 18))

    with open('notes_directory\\laser_results.txt', "w") as file:
        file.write(parameter_display)
        file.close()
    os.startfile('notes_directory\\laser_results.txt')


parameterBtn = ttk.Button(laser_frame, text='Calculate', command=parameters)
parameterBtn.place(x=15, y=257, height=30, width=100)

window.mainloop()
