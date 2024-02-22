#include <iostream>
#include <limits> 
using namespace std;

int main()
{
    string name;
    float salary, kilometres, hours, contributions;

    float x = 1;
    while (x <= 15) {
        cout << "You are using the Microsoft payment system" << endl;
        cout << "Enter employee name" << endl;
        cin >> name;

        cout << "Enter the salary" << endl;
        while (!(cin >> salary)) {

            cout << "Error: Please enter a valid numerical value for salary." << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }

        cout << "Distance Travelled in Kilometres" << endl;
        while (!(cin >> kilometres)) {
        
            cout << "Error: Please enter a valid numerical value for kilometres." << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }

        cout << "Overtime hours" << endl;
        while (!(cin >> hours)) {
        
            cout << "Error: Please enter a valid numerical value for hours." << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }

        cout << "Sundry Contributions" << endl;
        while (!(cin >> contributions)) {
            
            cout << "Error: Please enter a valid numerical value for contributions." << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }

        cout << "Employee name:" << name << endl;

        float num1 = kilometres * 3;
        float num2 = hours * ((salary / 168) * 1.5);
        float num3 = salary;
        float num4 = contributions;
        float num5 = num1 + num2 + num3 + num4;

        cout << "Total Salary: " << "R" << num5 << endl;
        x++;
    }

    return 0;
}
