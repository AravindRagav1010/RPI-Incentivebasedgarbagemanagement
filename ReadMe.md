An Incentive based Garbage Management System using IoT

Hello!

This Garbage management system segregates the waste disposed by the user [paper and plastic waste] and provides incentives based on the amount of waste the user inputs. This system requires the user to place the waste, either paper or plastic on the lid of the bin, one by one. These are then segregated into designated bins. The segregation process will be performed by the Raspberry Pi module, using Machine Learning. The segregated wastes are then weighed, and the user is awarded with incentives accordingly, i.e., money is credited in the user's e-wallet. 
The amount of garbage in each bin can be monitored through a Mobile Application. This application will also notify the users when the bins are full. To ensure timely replacement of bins, the authorities are notified when either of the bins reach the threshold. 
If, however the bins are not replaced on time and either of the bins are full, the system prevents any kind of input, be it paper waste or plastic from the user. For example, if the bin designated for paper waste is full, the system blocks input. Therefore, garbage overflow can also be prevented. 
Thus, this system will help promote recycling and prevent improper waste disposal. 

Process or flow:

1.User opens the app, and gets his QR code ready to signin to the bin for disposal
2.Then the program starts and first it displays Garb-e fo 2 secs
3.Then camera turns onn and scans the QR and displays User logged in! + the user Id 
4.The the img processing works --> cam starts to capture waste images and ml model classifies the type of waste
5.The respective assigned bin lid opens for the user to dispose their waste
6.Next the ultrasonic sensor calculates the depth of the bin and returns if the bin is full or empty/half full
7.LCD displays the bin status
8.LED Binks 
----------- 1 iteration gets over...
