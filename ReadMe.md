An Incentive-based Smart Garbage Management System using IoT  
Garby  
  
This Garbage management system segregates the waste (4 types: Paper, Plastic, Glass, and Metal) disposed of by the user and provides incentives based on the amount of waste the user disposes.  
This system requires the user to show the waste, one by one. These are then segregated into designated bins based on the type of waste. The segregation process will be performed by the Raspberry Pi module, using the ResNet50 CNN model. Based on the segregated waste, the user is awarded incentives accordingly, i.e., money is credited to the user's e-wallet.   
The amount of garbage disposed by a user can be monitored through a Mobile Application.  
If however the bins are not replaced on time or the bins are full, then it is indicated with a red led so that the user won't dispose of that type of waste. Therefore, garbage overflow can also be prevented.   
Thus, this system will help promote recycling and prevent improper waste disposal while creating awareness by incentivizing their efforts in proper disposal.   
  
Process or flow:  
  
1. User opens the app and gets his QR code ready to sign in to the bin for disposal.  
2. Then the program starts and first it displays "Garb-e" and the status of the bins for 2 secs.  
3. Then the camera turns on and scans the QR and displays User logged in! along with the user ID.  
4. Image processing --> cam starts to capture waste images and the CNN model identifies the type of waste.  
5. Segregation --> The respective bin assigned to the waste that is been identified opens for the user to dispose of their waste.  
6. Level Detection --> The ultrasonic sensor calculates the depth of the bin and returns if the bin is full or empty/half full and indicated using the LEDs.  
7. Provision of Incentive --> The user is been incentivized with credits that correspond to the type of waste that is been disposed of.  
----------- This process takes place until the user wants to stop disposing of the waste -----------
