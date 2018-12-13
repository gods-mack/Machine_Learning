#include<iostream>
#include<vector>

#include<cmath>

using namespace std;


void gradient_descent(vector<double> &x, vector<double> &y,int n)
{
double ss=0; // sum of squere
double sp=0; // sum of product;
double mx=0; // Mean of x's value
double my=0; // mean of Y's value
double m; // slope'
double c; // intercept

for(int i=0;i<n;i++)
 { mx = mx + x[i];
   my = my + y[i]; 

 }
 mx = mx/n;
 my = my/n;

for(int i=0;i<n;i++)
 {  
   ss = ss + pow(x[i]-mx,2);
  }

 for(int i=0;i<n;i++)
 {    
   sp = sp + (x[i]-mx) * (y[i]-my) ;
 }
   
 m = sp/ss;
 c = my - m*mx;

for(int i=0;i<n;i++)
 { cout<<" yp "<<m*x[i]+c<< " x "<<x[i]<<endl;
 }
cout<<endl;
 cout<<" slope "<<m<<" intercept "<<c<<endl;
 

}


int main()
{
  int n; 
  cin>>n;
 vector<double> x(n);
 vector<double> y(n);

for(int i=0;i<n;i++)
 { cin>>x[i]>>y[i]; }

gradient_descent(x,y,n);

}

