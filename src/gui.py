from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from src.HataModel import HataModel
from src.Cell import Cell

# For Input data field
def createEntry(root, row, col):
    entry = Entry(root, bg='light cyan', fg='black', font=("Arial", 14))
    entry.grid(row=row, column=col, sticky='e')
    entry.focus_force()
    return entry

# For Input field label
def createLabel(root, text, row, col):
    label = Label(root, text=text, bg='snow', fg='midnight blue', font=("Helvetica", 14, 'bold'))
    label.grid(row=row, column=col, columnspan=50, padx=50, pady=10, sticky='w')
    label.focus_force()
    return label

# For Output variable
def createOutputLabel(root, text, row, col):
    label = Label(root, text=text, bg='floral white', fg='blue', font=("Helvetica", 16, 'bold'))
    label.grid(row=row, column=col, columnspan=50, padx=50, pady=10, sticky='w')
    label.focus_force()
    return label


def pop_upp(type):
    if type == 'error1':
        return messagebox.showerror(message='Please enter the valid value')
    if type == 'error2':
        return messagebox.showerror(message='Please enter the value of all field')


def create_task_frame(task=1):
    frame = Frame(width=1100, height=600)
    # img = PhotoImage(Image.open('../img/theme1.jpg'))
    # frame.config(image=img)
    if task == 1:
        frame.config(bg='gray25')


        # Input text
        total_area_input_text = 'Enter the value of total area cover (in km): '
        total_number_of_traffic_channels_input_text = 'Enter the number of total traffic channels: '
        cell_type_input_text = 'Select the cell type : '
        radius_of_cell_input_text = 'Enter the radius of each cell ( Macro-cell(1-20km) , Micro-cell(.1-1km)): '
        frequency_reuse_factor_input_text = 'Enter the frequency reuse factor (1 , 3 , 4, 7, 9, 12, 13, 16 , 19, 21):'
        cell_type_options = ['Macro-cell', 'Micro-cell']
        freq_reuse_valid_values = [1, 3, 4, 7, 9, 12, 13, 16, 19, 21]

        # Output variable declaration
        total_area = StringVar()
        total_number_of_traffic_channel = StringVar()
        cell_type = StringVar()
        radius_of_the_cell = StringVar()
        frequency_reuse_factor = StringVar()
        cell_type_clicked = StringVar()

        def clear_screen1():
            total_area.delete(0, 'end')
            total_number_of_traffic_channel.delete(0, 'end')
            radius_of_the_cell.delete(0, 'end')
            frequency_reuse_factor.delete(0, 'end')

        # Cell Structure output
        def get_cell_outputs():

            # initialize a bool variable for checking error
            ok = True

            try:
                total_area_val = float(total_area.get())
                total_number_of_traffic_channel_val = int(total_number_of_traffic_channel.get())
                radius_of_the_cell_val = float(radius_of_the_cell.get())
                frequency_reuse_factor_val = int(frequency_reuse_factor.get())

                # Checking the radius range of cell for the cell type
                # if the radius of the cell is out of the range with the associated type
                # set ok = False
                if cell_type_clicked.get() == 'Macro-cell':
                    if radius_of_the_cell_val < 1.0 or radius_of_the_cell_val > 20.0:
                        response = messagebox.showinfo('Error', 'Enter the value between (1-20km) for  Macro-cell')
                        Label(frame, text=response).pack()
                        ok = False
                else:
                    if radius_of_the_cell_val < 0.1 or radius_of_the_cell_val > 1.0:
                        response = messagebox.showinfo('Error', 'Enter the value between (1-20km) for  Micro-cell')
                        Label(frame, text=response).pack()
                        ok = False

                if frequency_reuse_factor_val not in freq_reuse_valid_values:
                    response = messagebox.showinfo('Error', 'Enter the valid input')
                    Label(frame, text=response).pack()
                    ok = False

                # if no value error occurs
                if ok:
                    cell = Cell(total_area=total_area_val,
                                total_number_of_traffic_channels=total_number_of_traffic_channel_val,
                                radius_of_cell=radius_of_the_cell_val, frequency_reuse_factor=frequency_reuse_factor_val)
                    clear_screen1()
                    # Output
                    output_text1 = 'The number of required cells: ' + str(cell.number_of_cells) + ' cells'
                    output_text2 = 'The number of channels per cell: ' + str(
                        cell.number_of_channels_per_cell) + ' channels/cell'
                    output_text3 = 'Total capacity: ' + str(cell.total_capacity) + ' channels'
                    output_text4 = 'Total number of possible concurrent call: ' + str(
                        cell.total_number_of_possible_concurrent_call)

                    createOutputLabel(frame, output_text1, 6, 0)
                    createOutputLabel(frame, output_text2, 7, 0)
                    createOutputLabel(frame, output_text3, 8, 0)
                    createOutputLabel(frame, output_text4, 9, 0)
                else:
                    response = messagebox.showinfo('Error', 'Please fill up all the field value with valid data')
                    Label(frame, text=response).pack()
            except ValueError as e:
                response = messagebox.showinfo('Error', 'Please fill up all the field value')
                Label(frame, text=response).pack()

        # Input label and entry for total area covered
        createLabel(frame, total_area_input_text, 0, 0)
        total_area = createEntry(frame, 0, 52)

        # For total traffic channels
        createLabel(frame, total_number_of_traffic_channels_input_text, 1, 0)
        total_number_of_traffic_channel = createEntry(frame, 1, 52)

        # For cell type
        createLabel(frame, cell_type_input_text, 2, 0)
        ttk.Style().configure('TMenubutton', background="light yellow", font=('Helvetica', 16, 'bold'))
        cell_type_clicked.set(cell_type_options[0])
        cell_size = OptionMenu(frame, cell_type_clicked, *cell_type_options)
        cell_size.grid(row=2, column=52, padx=50, pady=20)

        # For radius of the cell
        createLabel(frame, radius_of_cell_input_text, 3, 0)
        radius_of_the_cell = createEntry(frame, 3, 52)

        # For frequency reuse factor
        createLabel(frame, frequency_reuse_factor_input_text, 4, 0)
        frequency_reuse_factor = createEntry(frame, 4, 52)

        # Output button
        output_button = Button(frame, text='Get Outputs', font=('Helvetica', 16, 'bold'), justify=CENTER, bg='ghost white', command=get_cell_outputs)
        output_button.grid(row=5, column=10, padx=100, pady=20)

        # Clear button
        clear_button = Button(frame, text='Clear', font=('Helvetica', 16, 'bold'), bg='ghost white', command=clear_screen1)
        clear_button.grid(row=5, column=32, padx=100, pady=20)

    else:

        # Define frame background color
        frame.config(bg='slate blue')

        # Declaring input text
        carrier_freq_input_text = 'Enter the value of carrier frequency(150-1500 in MHz): '
        base_station_antenna_height_input_text = 'Enter the height of transmitter antenna (30 - 300 in meter): '
        mobile_station_antenna_height_input_text = 'Enter the height of receiver antenna (1 - 10 in meter): '
        propagation_distance_input_text = 'Enter the distance between antennas (1 - 20 in km): '
        city_size_type_input_text = 'Select the city city size: '
        area_type_input_text = 'Select the area type: '
        city_size_options = ['Small/Medium', 'Large']
        area_type_options = ['Urban', 'Suburban', 'Open area']

        # Initialize output variable
        carrier_freq = StringVar()
        base_station_antenna_height = StringVar()
        mobile_station_antenna_height = StringVar()
        propagation_distance = StringVar()
        city_size_checked = StringVar()
        area_type_checked = StringVar()
        # path_loss = StringVar()

        # Input label and entry for taking carrier frequency
        createLabel(frame, carrier_freq_input_text, 0, 0)
        carrier_freq = createEntry(frame, 0, 52)

        # Base antenna height
        createLabel(frame, base_station_antenna_height_input_text, 1, 0)
        base_station_antenna_height = createEntry(frame, 1, 52)

        # Receiver antenna height
        createLabel(frame, mobile_station_antenna_height_input_text, 2, 0)
        mobile_station_antenna_height = createEntry(frame, 2, 52)

        # Propagation path distance
        createLabel(frame, propagation_distance_input_text, 3, 0)
        propagation_distance = createEntry(frame, 3, 52)

        # City size - Small/Medium, Large
        createLabel(frame, city_size_type_input_text, 4, 0)
        city_size_checked.set(city_size_options[0])
        city_size = OptionMenu(frame, city_size_checked, *city_size_options)
        city_size.grid(row=4, column=52, padx=10, pady=10)


        # Area type - Urban/Suburban, Open area
        createLabel(frame, area_type_input_text, 5, 0)
        area_type_checked.set(area_type_options[0])
        area_type = OptionMenu(frame, area_type_checked, *area_type_options)
        area_type.grid(row=5, column=52, padx=10, pady=10)


        # Clear all field value for frame 2
        def clear_screen2():
            carrier_freq.delete(0, 'end')
            base_station_antenna_height.delete(0, 'end')
            mobile_station_antenna_height.delete(0, 'end')
            propagation_distance.delete(0, 'end')

        # Output scope
        def get_path_loss():
            city_size_val = 0
            area_type_val = 0
            if city_size_checked.get() == 'Small/Medium':
                city_size_val = 1
            else:
                city_size_val = 2
            if area_type_checked.get() == 'Urban':
                area_type_val = 1
            elif area_type_checked.get() == 'Suburban':
                area_type_val = 2
            else:
                area_type_val = 3
            try:
                carrier_freq_val = float(carrier_freq.get())
                base_station_antenna_height_val = float(base_station_antenna_height.get())
                mobile_station_antenna_height_val = float(mobile_station_antenna_height.get())
                propagation_distance_val = float(propagation_distance.get())

                # Check the validity of input data
                ok = True
                if carrier_freq_val < 150.0 or carrier_freq_val > 1500.0:
                    response = messagebox.showinfo('Error', 'Enter the valid input')
                    Label(frame, text=response).pack()
                    ok = False
                if base_station_antenna_height_val < 30.0 or base_station_antenna_height_val > 300.0:
                    response = messagebox.showinfo('Error', 'Enter the valid input')
                    Label(frame, text=response).pack()
                    ok = False
                if mobile_station_antenna_height_val < 1 or mobile_station_antenna_height_val > 10:
                    response = messagebox.showinfo('Error', 'Enter the valid input')
                    Label(frame, text=response).pack()
                    ok = False
                if propagation_distance_val < 1 or propagation_distance_val > 20:
                    response = messagebox.showinfo('Error', 'Enter the valid input')
                    Label(frame, text=response).pack()
                    ok = False
                if ok:
                    model = HataModel(carrier_frequency=carrier_freq_val,
                                      height_transmitter=base_station_antenna_height_val,
                                      height_receiver=mobile_station_antenna_height_val,
                                      link_distance=propagation_distance_val, city_size_val=city_size_val,
                                      area_type_val=area_type_val)


                    # print(model.path_loss)
                    # Clear the all input-field for frame 2
                    clear_screen2()
                    output_text = 'The total predicted path loss (in decibel): ' + str(round(model.path_loss, 3)) + ' dB'

                    # Output label
                    createOutputLabel(frame, output_text, 8, 0)

                else:
                    response = messagebox.showinfo('Error', 'Please fill up all the field value with valid data')
                    Label(frame, text=response).pack()

            except ValueError as e:
                response = messagebox.showinfo('Error', 'Please fill up all the field value')
                Label(frame, text=response).pack()

        #
        output_button = Button(frame, text='Get Output', font=('Helvetica', 16, 'bold'), bg='ghost white', command=get_path_loss)
        output_button.grid(row=7, column=10, padx=100, pady=20)

        clear_button = Button(frame, text='Clear', font=('Helvetica', 16, 'bold'), bg='ghost white', command=clear_screen2)
        clear_button.grid(row=7, column=32, padx=100, pady=20)
    frame.pack()

    return frame


def create_TkWindow(height, width):
    root = Tk()
    root.geometry('%dx%d' % (width, height))
    root.iconbitmap('../img/flock.ico')
    # custom style
    style = ttk.Style()
    style.configure('TEntry', foreground='green')
    style.theme_create("aqua", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [0, 5, 5, 0]}},
        "TNotebook.Tab": {
            "configure": {"padding": [10, 10], "background": 'SlateBlue', "foreground": "ghost white"},
            "map": {"background": [("selected", 'green')],
                    "expand": [("selected", [1, 1, 1, 0])]}}})

    style.theme_use("aqua")
    return root


def create_Notebook(root):
    notebook = ttk.Notebook(root)

    def quit_root():
        response = messagebox.askyesno('Quit?', 'Do you want to quit?')
        Label(root, text=response).pack()
        if response:
            root.destroy()
        else:
            pass

    frame1 = create_task_frame(task=1)
    quit_button = Button(frame1, text='Quit', command=quit_root, font=('Helvetica', 16, 'bold'))
    quit_button.grid(row=5, column=52, padx=100, pady=20)
    frame2 = create_task_frame(task=2)
    quit_button = Button(frame2, text='Quit', command=quit_root, font=('Helvetica', 16, 'bold'))
    quit_button.grid(row=7, column=52, padx=100, pady=20)
    notebook.add(frame1, text='Cell Structure',)
    notebook.add(frame2, text='Hata Model ')

    return notebook.pack(expand=1, fill='both')


# Main Function
root = create_TkWindow(600, 1100)
notebook = create_Notebook(root)

root.mainloop()
