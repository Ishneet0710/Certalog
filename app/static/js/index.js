function deleteCert(certId) {
    fetch('/delete', {
        method: 'POST',
        body: JSON.stringify({ certId: certId }),
    }).then((_res) => {
        // Note: can change this URL to any endpoint you'd like
        window.location.href = "/catalog"
    });
}