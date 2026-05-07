import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
  stages: [
    { duration: '1m', target: 50000 },  // Ramp-up to 100 users over 1 minute
    { duration: '40m', target: 10000 },  // Stay at 100 users for 3 minutes
    { duration: '3m', target: 0 },    // Ramp-down to 0 users
  ],
};

export default function () {
  http.get('https://anmol-brij-divine-project.vercel.app'); // Replace with your site's URL
  sleep(1); // simulate user wait time
}

/*

Here’s a basic JavaScript (Node.js) code using the popular k6 tool to stress test a website. k6 is a performance testing tool written in Go, but the scripts are written in JavaScript.

✅ Step 1: Install k6
Make sure you have k6 installed. If not, install it using:
choco install k6   # Windows (using Chocolatey)
brew install k6    # macOS (using Homebrew)


✅ Step 2: Run the test
In terminal:

k6 run test.js

⚠️ Caution: Simulating 10,000 users will consume high system/network resources. Use this wisely, preferably on staging environments.


*/