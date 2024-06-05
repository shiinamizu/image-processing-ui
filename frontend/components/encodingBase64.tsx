function base64Decode(imgData) {
    // arraybuffer で渡された imgData を base64 エンコードする
    const base64Decoded = imgData.toString('base64');
    console.log(base64Decoded)
    return base64Decoded;
  }

  export {base64Decode}