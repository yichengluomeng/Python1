#include<stdio.h>

int Add(int x,int y)
{
	int z = 0;
	z = x + y;
	return z;
}

int main()
{
	int num1 = 0, num2 = 0,sum = 0;
	scanf_s("%d%d", &num1, &num2);
	sum = Add(num1,num2);
	printf("%d", sum);
	return 0;
}