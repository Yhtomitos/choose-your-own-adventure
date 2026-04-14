(function () {
  const isGithubPages = window.location.hostname.endsWith('github.io');
  window.CYOA_API_BASE = isGithubPages ? 'https://cyoagroup2.netlify.app' : '';
})();
