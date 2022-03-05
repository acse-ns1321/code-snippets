// pointers of arrays to use as arguments for a function


void generateArray(int *a, int si)
{
    for (int j = 0; j < si; j++)
        a[j] = rand() % 9;
}

int main()
{
    const int size=5;
    int a[size];

    generateArray(a, size);

    return 0;
}