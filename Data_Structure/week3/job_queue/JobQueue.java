import java.io.*;
import java.util.*;

public class JobQueue {
    private int numWorkers;
    private int[] jobs;

    private int[] assignedWorker;
    private int[] assignedWorker_naive;
    private long[] startTime;
    private long[] startTime_naive;

    private FastScanner in;
    private PrintWriter out;

    public static void main(String[] args) throws IOException {
       new JobQueue().solve();
        //   new JobQueue().stressTest();
    }

    private void readData() throws IOException {
        numWorkers = in.nextInt();
        int m = in.nextInt();
        jobs = new int[m];
        for (int i = 0; i < m; ++i) {
            jobs[i] = in.nextInt();
        }
    }

    private void writeResponse() {
        for (int i = 0; i < jobs.length; ++i) {
            out.println(assignedWorker[i] + " " + startTime[i]);
        }
    }

    private void assignJobs_naive() {
        // TODO: replace this code with a faster algorithm.
        assignedWorker_naive = new int[jobs.length];
        startTime_naive = new long[jobs.length];
        long[] nextFreeTime = new long[numWorkers];
        for (int i = 0; i < jobs.length; i++) {
            int duration = jobs[i];
            int bestWorker = 0;
            for (int j = 0; j < numWorkers; ++j) {
                if (nextFreeTime[j] < nextFreeTime[bestWorker])
                    bestWorker = j;
            }
            assignedWorker_naive[i] = bestWorker;
            startTime_naive[i] = nextFreeTime[bestWorker];
            nextFreeTime[bestWorker] += duration;
        }
    }

    private void assignJobs(){
        PriorityQueue<Worker> pq = new PriorityQueue<>(numWorkers,
                new Comparator<Worker>() {
            @Override
            public int compare (Worker w1, Worker w2) {
                if(w1.nextFreeTime == w2.nextFreeTime) {
                    return (int)(w1.id - w2.id);
                } else {
                    return (int)(w1.nextFreeTime - w2.nextFreeTime);
                }
            }
        });

        // Push all workers into qp
        for(int i = 0; i < numWorkers; i++) {
            pq.offer(new Worker(i));
        }

        assignedWorker = new int[jobs.length];
        startTime = new long[jobs.length];


        // Process each job for the freeThread (have less nextFreeTime)
        for(int j = 0; j < jobs.length; j++) {
            Worker freeThread = pq.poll();
            // Record Job j's assigned worker and startTime
            assignedWorker[j] = freeThread.id;
            startTime[j] = freeThread.nextFreeTime;
            // Update next free time
            freeThread.nextFreeTime += jobs[j];
            // push back to the pq
            pq.offer(freeThread);
        }
    }

    private static class Worker {
        int id;
        long nextFreeTime;
        public Worker (int id) {
            this.id = id;
            nextFreeTime = 0;
        }
    }

    public void solve() throws IOException {
        in = new FastScanner();
        out = new PrintWriter(new BufferedOutputStream(System.out));
        readData();
        assignJobs();
        writeResponse();
        out.close();
    }

    public void stressTest() {
        // Generate random m threads and array of n jobs
        // Compare naive and faster algorithm
        Random random = new Random();
        int bound = 100000, job_bound = 1000000000;
        while(true) {
            this.numWorkers = random.nextInt(bound) + 1;
            int m = random.nextInt(bound) + 1;
            jobs = new int[m];
            for(int i = 0; i < m; i++) {
                jobs[i] = random.nextInt(job_bound);
            }
            long start = System.currentTimeMillis();
            assignJobs();
            long end = System.currentTimeMillis();
            assignJobs_naive();
            if(Arrays.equals(assignedWorker,assignedWorker_naive)&&
                    Arrays.equals(startTime, startTime_naive)) {
                System.out.println("OK: n = " + numWorkers + "\t" + (end - start) + " ms.");
            } else {
                System.out.println("Error: n = " +numWorkers);
            }

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
