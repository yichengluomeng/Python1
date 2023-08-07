#include<stdio.h>

int main()
{
	int a = 1;
	int b = (++a) + (++a) + (++a);
	printf("%d\n", b);
	return 0;
}