function GrepContent() {
      let _collection = document.getElementsByClassName('rendered')[0].children,
              _content = '';
      for ( let item in _collection) {
              let tag = _collection[item];
              if(tag.tagName === 'H2') {
                        return _content;
                      }
              else {
                        _content += tag.innerText;
                      };
            };
}
