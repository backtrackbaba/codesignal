'''

You're probably used to measuring temperature in Celsius degrees, but there's also a lesser known temperature scale called Fahrenheit, which is used in only 5 countries around the world.

You can convert a Celsius temperature (C) to Fahrenheit (F), by using the following formula:

F = 9 * C / 5 + 32

Your friend lives in Palau (where the Fahrenheit system is used), and you've been trying to find out which of you lives in a warmer climate, so you've each kept track of your respective daily temperatures for the past n days.

Given two arrays of integers yourTemps and friendsTemps (each of length n), representing the local daily temperatures (in Celsius and Fahrenheit, respectively), find how many days were hotter in Palau.

Example

For yourTemps = [25, 32, 31, 27, 30, 23, 27] and friendsTemps = [78, 83, 86, 88, 86, 89, 79], the output should be celciusVsFahrenheit(yourTemps, friendsTemps) = 3.

Converting your recorded temperatures to Fahrenheit gives the results [77, 89.6, 87.8, 80.6, 86, 73.4, 80.6], which can be compared to the temperatures your friend recorded:

your temps	friend's temps
77	            78
89.6	        83
87.8	        86
80.6	        88
86	            86
73.4	        89
80.6	        79
There were 3 days where your friend recorded hotter temperatures, so the answer is 3.

[execution time limit] 4 seconds (py3)

[input] array.integer yourTemps

An array of integer representing the daily temperatures you recorded in Celcius degrees.

Guaranteed constraints:
1 ≤ yourTemps.length ≤ 365
-50 ≤ yourTemps[i] ≤ 50

[input] array.integer friendsTemps

An array of integers representing the daily temperatures your friend recorded in Fahrenheit degrees.

Guaranteed constraints:
friendsTemps.length = yourTemps.length
-58 ≤ friendsTemps[i] ≤ 122

[output] integer

An integer representing the number of days on which your friend recorded a higher temperature than you did.

'''


def celsiusVsFahrenheit(yourTemps, friendsTemps):

    new_yourTemp = []
    count = 0
    for i in range(len(yourTemps)):
        if friendsTemps[i] > ((yourTemps[i]*9/5) + 32):
            count = count+1
        

    return count


yourTemps = [25, 32, 31, 27, 30, 23, 27]
friendsTemps = [78, 83, 86, 88, 86, 89, 79]
print(celsiusVsFahrenheit(yourTemps, friendsTemps))