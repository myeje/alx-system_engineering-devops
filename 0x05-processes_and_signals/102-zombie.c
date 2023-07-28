#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - function that creates an infinite loop
 * with its PID
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - runs the process
 * Return: 0
 */
int main(void)
{
	pid_t process;
	int i;

	for (i = 0; i < 5; i++)
	{
		process = fork();
		if (process > 0)
			printf("Zombie process created, PID: %d\n", process);
		else if (process == 0)
			exit(0);
		else
			exit(1);
	}
	infinite_while();
	return (0);
}
