/**
 * linearsearch
 */
public class linearsearch {

    public static int ara(int arr[], int x) {
        int n = arr.length;
        for(int i = 0; i < n; i++){
            if(arr[i] == x)
                return i;
        }
        return -1;
    }

    public static void main(String args[]) {
        int arr[] = {2, 3, 4, 5, 6};
        int x = 4;

        int sonuc = ara(arr, x);
        if(sonuc == -1)
            System.out.print("Element is not present in array"); 
        else
            System.out.print("Element is present at index " + sonuc); 
    }
}