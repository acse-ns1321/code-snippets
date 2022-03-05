#include<bits/stdc++.h>

using namespace std;
//Implement the class Box  
class Box {
        
    // Class variables l,b,h are integers representing the dimensions of the box
    private:
    int l, b, h;
    
    public:

    // Constructors: 
    
    // Default Constructor-- Box();
    Box(){
        l = 0;
        b = 0;
        h = 0;
    }

    // Parameterized Constructor -- Box(int,int,int);
    Box(int length, int breadth, int height) {
        this->l = length;
        this->b = breadth;
        this->h = height;
    }
    // Copy Constuctor -- Box(Box);
    Box(const Box &B){
        this->l = B.l;
        this->b = B.b;
        this->h = B.h;
    };

    // Class Methods
    
    // Getters
    
    // Return box's length
    int getLength() const {
    return l;
    };
    // Return box's breadth
    int getBreadth () const {
    return b;    
    };
    // Return box's height
    int getHeight () const {
    return h;
    }; 
    // Return the volume of the box
    long long CalculateVolume(){
        return (long long)l*b*h; // assign variable type t the result to pass al the tests
    };
    
    //Overload operator < as specified
    bool operator<(Box& B){
        if ( (B.l > l) || (B.b > b && B.l == l) || 
        (B.h > h && B.b == b & B.l == l) ) {
        return true;
        }
        else {
        return false;
        }
    };

    //Overload operator << as specified
    friend ostream& operator<<(ostream& COUT, Box& B){
        COUT << B.l << " " << B.b << " " << B.h ;
        return COUT;
};
};

void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl;
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl;
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;
		}

	}
}

int main()
{
	check2();
}