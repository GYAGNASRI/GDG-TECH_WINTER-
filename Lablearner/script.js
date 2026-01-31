function explainCode() {
  const code = document.getElementById('codeInput').value;
  const language = document.getElementById('language').value;

  fetch('/api/explain', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({code, language})
  })
  .then(r => r.json())
  .then(data => {
      document.getElementById('explanation').innerHTML = 
          `<strong>Explanation (${data.language}):</strong><p>${data.explanation}</p>`;
  });
}

function getPractice() {
  const topic = document.getElementById('topic').value;

  fetch('/api/practice', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({topic})
  })
  .then(r => r.json())
  .then(data => {
      const html = data.problems
          .map(p => `<li>${p}</li>`)
          .join('');
      document.getElementById('practiceList').innerHTML = html;
  });
}

function showFutureCourses() {
  fetch('/api/future-courses')
      .then(r => r.json())
      .then(data => {
          let html = '';
          for (let topic in data) {
              html += `<li><strong>${topic}:</strong> ${data[topic].join(', ')}</li>`;
          }
          document.getElementById('coursesList').innerHTML = html;
      });
}
