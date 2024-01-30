#!/usr/bin/node
const request = require('request');

function computeCompletedTasks (apiUrl) {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(`Error: ${error.message}`);
    } else if (response.statusCode !== 200) {
      console.error(`Request failed with status code: ${response.statusCode}`);
    } else {
      const tasks = JSON.parse(body);

      const completedTasksCountByUser = new Map();

      tasks.forEach(task => {
        if (task.completed) {
          const userId = task.userId;
          completedTasksCountByUser.set(userId, (completedTasksCountByUser.get(userId) || 0) + 1);
        }
      });

      const resultObject = {};
      completedTasksCountByUser.forEach((count, userId) => {
        resultObject[userId] = count;
      });

      console.log(resultObject);
    }
  });
}

const [,, apiUrl] = process.argv;
computeCompletedTasks(apiUrl);
