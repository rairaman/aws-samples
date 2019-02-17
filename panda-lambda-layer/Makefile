PKG_DIR=panda-layer/panda-bin

clean:
	rm -rf $(PKG_DIR)/*

compile-panda: clean
	docker run --rm -u 1000:1000 -v "$(PWD)":/tmp -w /tmp lambci/lambda:build-python3.6 pip install -r requirements.txt --no-deps -t $(PKG_DIR)