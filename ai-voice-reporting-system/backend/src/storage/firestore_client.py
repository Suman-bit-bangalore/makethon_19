from google.cloud import firestore

class FirestoreClient:
    def __init__(self):
        self.db = firestore.Client()

    def add_summary(self, collection_name, document_id, summary_data):
        self.db.collection(collection_name).document(document_id).set(summary_data)

    def get_summary(self, collection_name, document_id):
        doc_ref = self.db.collection(collection_name).document(document_id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            return None

    def update_summary(self, collection_name, document_id, summary_data):
        self.db.collection(collection_name).document(document_id).update(summary_data)

    def delete_summary(self, collection_name, document_id):
        self.db.collection(collection_name).document(document_id).delete()