function [slope , intercept] = linearReg(x,y,n)
  
  mx=0;
  my=0;
  ss=0;
  sp=0;
  
  for i=1:n
    mx = mx + x(i);
  endfor
  mx = mx/n;
  
  for j=1:n
    my = my + y(j);
  endfor
  my = my/n;
  
  for k=1:n
    ss = ss + (x(k)-mx).^2 ;
  endfor
  
  for l=1:n
    sp = sp + (x(l)-mx) * (y(l)-my);
  endfor
  
  m = sp/ss;
  c = my - m*mx;
  
  yp=[];
  for t=1:n
    yp(t)=m*x(t)+c;
  endfor
  
  plot(x,y,'*');
  hold on;
  plot(x,yp);
  
  slope=m;
  intercept=c;
  
  
  
endfunction
