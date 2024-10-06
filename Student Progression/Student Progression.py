
passes=True
list1=[]
list2=[0,0,0,0]
count=[0,0,0,0]
values = [0, 20, 40, 60, 80, 100, 120]
#Histogram Function
from graphics import *;
#Graphics.py documentation as a Reference
def histogram():
            win = GraphWin('Histogram',800,600)
            win.setBackground("#E0EEE0")
            my_heading=Text(Point(150,50),'Histogram Results')
            my_heading.setStyle('bold')
            my_heading.setFace('helvetica')
            my_heading.setFill('#808A87')
            my_heading.setSize(24)
            my_heading.draw(win)
            max_value=max(list2)
            size = [value * (300 /max_value) for value in list2]
            aRectangle = Rectangle(Point(100, 500 - size[0]), Point(200, 500))
            bRectangle = Rectangle(Point(250, 500 - size[1]), Point(350, 500))
            cRectangle = Rectangle(Point(400, 500 - size[2]), Point(500, 500))
            dRectangle = Rectangle(Point(550, 500 - size[3]), Point(650, 500))
#Line at the bottom of the histogram
            aLine = Line(Point(50,500), Point(700,500))
            aRectangle.setFill('#97fb97')
            bRectangle.setFill('#96c783')
            cRectangle.setFill('#a2bd6e')
            dRectangle.setFill('#d8b5b4')
            aRectangle.draw(win)
            bRectangle.draw(win)
            cRectangle.draw(win)
            dRectangle.draw(win)
            aLine.draw(win)
#Text Labels at the bottom of the histogram
            label_progress = Text(Point(150, 520), "Progress")
            label_progress.setSize(18)
            label_progress.setFill('#838B8B')
            label_progress.setStyle('bold')
            label_progress.setFace('helvetica')

            label_trailer = Text(Point(300, 520), "Trailer")
            label_trailer.setSize(18)
            label_trailer.setFace('helvetica')
            label_trailer.setFill('#838B8B')
            label_trailer.setStyle('bold')

            label_retriver = Text(Point(450, 520), "Retriver")
            label_retriver.setSize(18)
            label_retriver.setFace('helvetica')
            label_retriver.setFill('#838B8B')
            label_retriver.setStyle('bold')
            
            label_exclude = Text(Point(600, 520), "Exclude")
            label_exclude.setSize(18)
            label_exclude.setFace('helvetica')
            label_exclude.setFill('#838B8B')
            label_exclude.setStyle('bold')

            label_progress.draw(win)
            label_trailer.draw(win)
            label_retriver.draw(win)
            label_exclude.draw(win)

            text_point = Point(350, 550)
#calculating the count of each output
            progress_count = Text(Point(150, 500 - size[0] - 10), [count[0]])
            trailer_count = Text(Point(300, 500 - size[1] - 10), [count[1]])
            retriver_count = Text(Point(450, 500 - size[2] - 10), [count[2]])
            exclude_count = Text(Point(600, 500 - size[3] - 10), [count[3]])
#Displaying the count above each rectangle
            progress_count.setSize(18)
            progress_count.setStyle('bold')
            progress_count.setTextColor('#838B8B')
            trailer_count.setSize(18)
            trailer_count.setStyle('bold')
            trailer_count.setTextColor('#838B8B')
            retriver_count.setSize(18)
            retriver_count.setStyle('bold')
            retriver_count.setTextColor('#838B8B')
            exclude_count.setSize(18)
            exclude_count.setStyle('bold')
            exclude_count.setTextColor('#838B8B')

            progress_count.draw(win)
            trailer_count.draw(win)
            retriver_count.draw(win)
            exclude_count.draw(win)
            
#Displaying the total count at the bottom of the graph
            total_count = (count[0] + count[1] + count[2] + count[3])
            total_count_text = Text(Point(150, 570), str(total_count)  + ' Outcomes in Total ')
            total_count_text.setSize(18)
            total_count_text.setStyle('bold')
            total_count_text.setTextColor('#838B8B')
            total_count_text.draw(win)
            win.getMouse()
            win.close()

# Menu of Decision
A=input('student(s) or a staff(t):')
if A.lower()=='s':
    while passes:
# Part 1 - (B) - Validation - Student
        credit_pass = input("\nPlease enter your credit at pass : ")
        try:
            credit_pass = int(credit_pass)
            if credit_pass not in values:
                print('out of range')
                continue
        except ValueError:
            print("Integer required")
            continue

        defer_pass = input("Please enter your credit at defer : ")
        try:
            defer_pass = int(defer_pass)
            if defer_pass not in values:
                print('out of range')
                continue
        except ValueError:
            print("Integer required")
            continue

        fail_pass = input("Please enter your credit at fail : ")
        try:
            fail_pass = int(fail_pass)
            if fail_pass not in values:
                print('out of range')
                continue
        except ValueError:
            print("Integer required")
            continue
# Part 1 - (A) - Outcomes (conditons) - Student       
        if credit_pass + defer_pass + fail_pass == 120:
            if credit_pass == 120:
                print("Progress")
            elif credit_pass == 100:
                print("Progress module-trailer")
            elif fail_pass >= 80:
                print("Exclude")
            else:
                print("Do not progress - module retriever")
            break
        else:
            print("Total Incorrect")
            continue

elif A.lower()=='t':
    while passes:
# Part 1 - (B) - Validation - Staff 
        credit_pass = input("\nPlease enter your credits at PASS : ")
        try:
            credit_pass = int(credit_pass)
            if credit_pass not in values:
                print('out of range')
                continue
        except ValueError:
            print("Integer required")
            continue

        defer_pass = input("Please enter your credit at DEFER : ")
        try:
            defer_pass = int(defer_pass)
            if defer_pass not in values:
             print('out of range')
             continue
        except ValueError:
            print("Integer required")
            continue

        fail_pass = input("Please enter your credit at FAIL : ")
        try:
            fail_pass = int(fail_pass)
            if fail_pass not in values:
             print('out of range')
             continue
        except ValueError:
            print("Integer required")
            continue

# Part 1 - (A) - Outcomes (conditons)
        if credit_pass + defer_pass + fail_pass == 120:
            if credit_pass == 120:
                  print("Progress")
                  list1.append(f'Progress - {credit_pass}, {defer_pass}, {fail_pass}')
                  list2[0]=list2[0]+1
                  count[0]=count[0]+1
            elif credit_pass == 100:
                  print("Progress (module trailer)")
                  list1.append(f'Progress (module-trailer) - {credit_pass}, {defer_pass}, {fail_pass}')
                  list2[1]=list2[1]+1
                  count[1]=count[1]+1
            elif fail_pass >= 80:
                  print("Exclude")
                  list1.append(f'Exclude - {credit_pass}, {defer_pass}, {fail_pass}')
                  list2[3]=list2[3]+1
                  count[3]=count[3]+1
            else:
                print("Module retriever")
                list1.append(f'Module retriever - {credit_pass}, {defer_pass}, {fail_pass}')
                list2[2]=list2[2]+1
                count[2]=count[2]+1
        else:
            print("Total Incorrect")
            continue
# Part 1 - (C) - Multiple Outcomes(loop)
        user = True
        while user:
                user_input = input("\nWould you like to enter another set of data? "
                                "\nEnter 'y' for yes or 'q' to quit and view results: ")
                if user_input.lower() == 'y':
                    user = False
                    passes=True
                elif user_input.lower() == 'q':
                    user = False
                    passes = False
                #Histogram Calling
                    histogram()  
# Part 2 - Displaying the list outputs of the inputs 
                    for item in list1:
                                print(item)

# Part 3 - Writing the outputs to a text file 
                    new_file_path = '/Users/sandaraapoorwa/Desktop/CW/new_file.txt'
                    with open(new_file_path, "w") as text_file:
                        for item in list1:
                            text_file.write(item + '\n')
                else:
                    print('Invalid Input')
                    continue
                break
        

    

    


    
