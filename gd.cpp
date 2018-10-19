#include<bits/stdc++.h>
#include<cmath>
using namespace std;

void gradient_descent(vector<double> x,vector<double> y,int n)
{
double y_p=0,cost=0,m=0,b=0;
double learning_rate=0.01;

for(int i=0;i<1000;i++)
{
 int idx=i%5;
 y_p=m*x[idx]+b;
 cost=((y_p-y[idx]));
 
 m=m-(cost*x[idx]*learning_rate);
 b=b-(cost*learning_rate);
 

cout<<" Y_predict -> "<<y_p<<" X -> "<<x[idx]<<endl;
}

}


int main()
{
int n; cout<<"Enter No. of Data sets: "<<endl;
cin>>n;
cout<<"Enter data sets: "<<endl;
vector<double> x(n);
vector<double> y(n);
for(int i=0;i<n;i++)
{ cin>>x[i]>>y[i]; }

gradient_descent(x,y,n);

}

