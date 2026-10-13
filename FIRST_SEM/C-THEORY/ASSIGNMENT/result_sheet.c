#include <stdio.h>

#define STUDENTS 5
#define SUBJECTS 5
#define NAME_LEN 50
#define PASS_MARK 35
void readStudents(int roll[], char name[][NAME_LEN], int marks[][SUBJECTS]) {
    for (int i = 0; i < STUDENTS; i++) {
        printf("\n--- Student %d ---\n", i + 1);
        printf("Roll number: ");
        scanf("%d", &roll[i]);
        printf("Name: ");
        scanf(" %49[^\n]", name[i]);
        for (int j = 0; j < SUBJECTS; j++) {
            do {
                printf("Marks in subject %d (0-100): ", j + 1);
                scanf("%d", &marks[i][j]);
                if (marks[i][j] < 0 || marks[i][j] > 100)
                    printf("Invalid! Enter marks between 0 and 100.\n");
            } while (marks[i][j] < 0 || marks[i][j] > 100);
        }
    }
}
int calculateTotal(int marks[]) {
    int sum = 0;
    for (int j = 0; j < SUBJECTS; j++)
        sum += marks[j];
    return sum;
}
float calculateAverage(int total) {
    return (float)total / SUBJECTS;
}
float calculatePercentage(int total) {
    return ((float)total / (SUBJECTS * 100)) * 100;
}
int checkResult(int marks[]) {
    for (int j = 0; j < SUBJECTS; j++)
        if (marks[j] < PASS_MARK)
            return 0;
    return 1;
}
void processResults(int marks[][SUBJECTS], int total[], float avg[],
                    float perc[], int pass[]) {
    for (int i = 0; i < STUDENTS; i++) {
        total[i] = calculateTotal(marks[i]);
        avg[i]   = calculateAverage(total[i]);
        perc[i]  = calculatePercentage(total[i]);
        pass[i]  = checkResult(marks[i]);
    }
}
void displayTable(int roll[], char name[][NAME_LEN], int marks[][SUBJECTS],
                  int total[], float avg[], float perc[], int pass[]) {
    printf("\n\n%-8s %-15s %5s %5s %5s %5s %5s %7s %8s %9s %7s\n",
           "Roll No", "Name", "S1", "S2", "S3", "S4", "S5",
           "Total", "Average", "Percent", "Result");
    for (int k = 0; k < 90; k++) printf("-");
    printf("\n");

    for (int i = 0; i < STUDENTS; i++) {
        printf("%-8d %-15s", roll[i], name[i]);
        for (int j = 0; j < SUBJECTS; j++)
            printf(" %5d", marks[i][j]);
        printf(" %7d %8.2f %8.2f%% %7s\n",
               total[i], avg[i], perc[i], pass[i] ? "PASS" : "FAIL");
    }
}
int main(void) {
    int roll[STUDENTS];
    char name[STUDENTS][NAME_LEN];
    int marks[STUDENTS][SUBJECTS];
    int total[STUDENTS], pass[STUDENTS];
    float avg[STUDENTS], perc[STUDENTS];
    readStudents(roll, name, marks);
    processResults(marks, total, avg, perc, pass);
    displayTable(roll, name, marks, total, avg, perc, pass);
    return 0;
}