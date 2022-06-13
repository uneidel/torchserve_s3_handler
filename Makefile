build-mar:	
	torch-model-archiver --model-name hdr --version 1.0 --model-file ./model.py \
	--serialized-file ./weights.pth --handler handler.py \
	--extra-files ./util.py  --force
	mkdir -p model_store
	mv  hdr.mar ./model_store/	
	
run-local-cpu:
	torchserve --stop --model-store model_store --models hdr=hdr.mar
	torchserve --start --model-store model_store --models hdr=hdr.mar --ts-config config.properties

stop: 
	torchserve --stop --model-store model_store --models hdr=hdr.mar

run: build-mar run-local-cpu
