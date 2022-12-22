function deleteNote(noteId) {  //Use Javascripts to deleteNote, will be used in home.html
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }