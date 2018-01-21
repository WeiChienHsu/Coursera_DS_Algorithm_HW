import java.io.*;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.StringTokenizer;

public class BuildHeap {
    private int[] data;
    private List<Swap> swaps;

    private FastScanner in;
    private PrintWriter out;

    public static void main(String[] args) throws IOException {
        new BuildHeap().solve();
    }

    private void readData() throws IOException {
        int n = in.nextInt();
        data = new int[n];
        for (int i = 0; i < n; ++i) {
          data[i] = in.nextInt();
        }
    }

    private void writeResponse() {
        out.println(swaps.size());
        for (Swap swap : swaps) {
          out.println(swap.index1 + " " + swap.index2);
        }
    }

    private void generateSwaps() {
        swaps = new ArrayList<Swap>();
        // Note 0-based index
        for (int i = data.length / 2; i >= 0; i--) {
            sink(i);
        }
    }
    /**Sink element i to maintain min-heap property.
     * <p>
     * Choose the smaller of left/right child, if any.
     * Terminate if i is already less than children.
     * Swap with the smaller child, record the swap.
     * Trace i downwards to the smaller children.
     * Terminate if i has no children.
     *
     * @param i the index where sinking begins
     */
    private void sink(int i) {
        int n = data.length;
        // While i has at least one left child
        while (i * 2 + 1 < n) {
            int j = i * 2 + 1;  // left child
            // Decide if right child exists and the smaller child
            j = (j + 1 < n && data[j + 1] < data[j]) ? j + 1 : j;
            // BZ: no swap if i == smallest child?
            if (data[i] <= data[j]) return;
            swaps.add(new Swap(i, j));
            int tmp = data[i];
            data[i] = data[j];
            data[j] = tmp;
            i = j;  // Forward i to its smaller child
        }
    }

    public void solve() throws IOException {
        in = new FastScanner();
        out = new PrintWriter(new BufferedOutputStream(System.out));
        readData();
        generateSwaps();
        writeResponse();
        out.close();
    }

    static class Swap {
        int index1;
        int index2;

        public Swap(int index1, int index2) {
            this.index1 = index1;
            this.index2 = index2;
        }
    }

    static class FastScanner {
        private BufferedReader reader;
        private StringTokenizer tokenizer;

        public FastScanner() {
            reader = new BufferedReader(new InputStreamReader(System.in));
            tokenizer = null;
        }

        public String next() throws IOException {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                tokenizer = new StringTokenizer(reader.readLine());
            }
            return tokenizer.nextToken();
        }

        public int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
    }
}
