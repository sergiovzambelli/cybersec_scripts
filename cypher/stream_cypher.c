#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Function declarations */
int getSize(char *array);
int hashCode(const char *str, int size);
void convertIntToBinaryArray(int num, int *arr, int *index);
void encryptStreamCipher(int key[], int data[], int encypted_data[],int data_size);
void decryptStreamCipher(int key[], int enc_data[], int data_size);
void convertCharToBinary(char c,int *binary_arr,int *index);
void convertStringToBinary(char *str,int *binary_arr, int *size);
void convertBinaryToString(int *data,char *array_string,int *index);
char convertBinaryToChar(char *str);
void displayIntArray(int *array, int size);
void displayCharArray(char *array, int size);

#define MAX_SIZE 10000

/*
  Take input, take a key, use the key in order to initialize the random generator
  and obtain a new key made of random numbers.
  Than, XOR the data and the key bits: this is the encrypted data.
  The decryption follows the same steps, but need the same key and the same random
  number generator. 
*/

int main(int argc, char **argv) {

    char array_string[MAX_SIZE];
    char ascii_key[MAX_SIZE];
    int data[MAX_SIZE];
    int key[MAX_SIZE];
    int encypted_data[MAX_SIZE];
    int seed;
    int key_int;
    int key_size = 0;
    int index;
    int data_size = 0;

    fprintf(stdout, "Enter data to encrypt, do not use spaces: \n");
    fscanf(stdin, "%s", array_string);

    convertStringToBinary(array_string,data,&data_size);

    fprintf(stdout, "\nEnter key to encrypt data with: \n");
    fscanf(stdin, "%s", ascii_key);

    /* Get hash code from the key */
    key_size = getSize(ascii_key);
    seed = hashCode(ascii_key, key_size);

    /* Set the key as seed to random number generator to create a key of random bits */
    srand(seed);
    key_int = rand();

    convertIntToBinaryArray(key_int, key, &index);

    /* (Binary data) XOR (Binary key) */
    encryptStreamCipher(key, data, encypted_data, data_size);

    printf("\nEncrypted Data: \n");
    displayIntArray(encypted_data,data_size);

    /* 9.Now, Decrypt data and verify initial data */
    decryptStreamCipher(key, encypted_data, data_size);

    memset(array_string,0,sizeof(array_string));
    convertBinaryToString(encypted_data,array_string,&data_size);

    printf("\nDecrypted Data in String: \n");
    displayCharArray(array_string,data_size);

    return 0;
}

int getSize(char *array) {
    int size = 0;
    int i = 0;
    while ((i != MAX_SIZE) && (array[i] != '\0')) {
        i++;
        size++;
    }
    return size;
}

int hashCode(const char *str, int size) {
    int hash = 0;
    for (int i = 0; i < size; i++) {
        hash = 31 * hash + str[i];
    }
    return hash;
}

void convertIntToBinaryArray(int num, int *arr, int *index) {
    if (num == 0 || *index >= MAX_SIZE)
        return;
    convertIntToBinaryArray(num / 2, arr, index);
    if (num % 2 == 0)
        arr[(*index)++] = 0;
    else
        arr[(*index)++] = 1;

}

void encryptStreamCipher(int key[], int data[], int encypted_data[],
        int data_size) {
    for (int i = 0; i < data_size; i++) {
        encypted_data[i] = data[i] ^ key[i];
    }
}

void decryptStreamCipher(int key[], int enc_data[], int data_size) {
    for (int i = 0; i < data_size; i++) {
        enc_data[i] = enc_data[i] ^ key[i];
    }
}

void convertStringToBinary(char *str,int *binary_arr,int *index) {
    *index=0;
    for (int i = 0; i<strlen(str); i++) {
        convertCharToBinary(str[i],binary_arr,index);
    }
}

void convertCharToBinary(char c,int *binary_arr,int *index) {
    for (int i = 7; i >= 0; --i) {
        binary_arr[*index]=((c & (1 << i)) ? 1 : 0);
        (*index)++;
    }
}

void convertBinaryToString(int *data,char *array_string,int *index){
    int data_size=*index;
    char char_array[data_size];
    *index=0;

    for(int i=0;i<data_size;i++){
        char_array[i]=(data[i] == 1?'1':'0');
    }

    for(int i=0;i<data_size;i=i+8){
        char sub_str[8];
        memcpy(sub_str,char_array+i,8);
        array_string[(*index)++]=convertBinaryToChar(sub_str);
    }
}

char convertBinaryToChar(char *str){
    char c=strtol(str,0,2);
    return c;
}

void displayIntArray(int *array, int size)
{
    for (int i = 0; i < size; i++) {
        printf("%d",array[i]);
    }
    printf("\n");
}

void displayCharArray(char *array, int size)
{
    for (int i = 0; i < size; i++) {
        printf("%c",array[i]);
    }
    printf("\n");
}