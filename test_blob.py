from azure.storage.blob import BlobServiceClient


def create_container_if_not_exists(blob_service_client, container_name):
    """
    コンテナが存在しない場合に作成する
    """
    container_client = blob_service_client.get_container_client(container_name)
    try:
        container_client.create_container()
        print(f"コンテナ '{container_name}' を作成しました。")
    except Exception as e:
        print(f"コンテナは既に存在します: {e}")
    return container_client


def upload_file(blob_client, local_file_name):
    """
    ローカルファイルを作成してBlobにアップロードする
    """
    # ローカルファイル作成と内容の書き込み
    with open(local_file_name, "w", encoding="utf-8") as file:
        file.write("This is a test file.")

    # ファイルをBlobにアップロード（上書き許可）
    with open(local_file_name, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    print(f"'{local_file_name}' をアップロードしました。")


def download_file(blob_client, local_file_name):
    """
    Blobからデータをダウンロードしてローカルに保存する
    """
    downloaded_blob = blob_client.download_blob().readall()
    downloaded_file_name = f"downloaded_{local_file_name}"

    with open(downloaded_file_name, "wb") as file:
        file.write(downloaded_blob)
    print(f"'{downloaded_file_name}' としてダウンロードしました。")


def main():
    # Azure Blob Storage接続情報の設定
    connection_string = "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://localhost:10000/devstoreaccount1;"
    container_name = "test"
    blob_name = "test.txt"
    local_file_name = "test.txt"

    # BlobServiceClientの作成
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # コンテナを作成（存在しなければ）
    create_container_if_not_exists(blob_service_client, container_name)

    # BlobClientの作成
    blob_client = blob_service_client.get_blob_client(
        container=container_name, blob=blob_name
    )

    # ファイルのアップロードとダウンロード
    upload_file(blob_client, local_file_name)
    download_file(blob_client, local_file_name)

    print("ファイルのアップロードとダウンロードが成功しました。")


if __name__ == "__main__":
    main()
