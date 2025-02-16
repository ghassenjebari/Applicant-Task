import { useState } from "react";

import { Button, TextInput } from "@mantine/core";

import { createPart } from "@/data/dataHandler";



interface AddPartFormProps {
  onPartAdded: () => void; 
}

const AddPartForm: React.FC<AddPartFormProps> = ({ onPartAdded }) => {
  const [name, setName] = useState<string>("");
  const [comment, setComment] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);


  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      await createPart({ name, comment });
      onPartAdded();
      setName("");
      setComment("");

    } catch (error) {
      console.error("Error adding part:", error);
    }
    setLoading(false);
  };

  return (
    
    <form onSubmit={handleSubmit}>
     

     <TextInput
    label="Part Name"
    placeholder="Enter part name..."
    value={name}
    required
    className="glass-inputModal"
    style={{ marginBottom: "16px" }} 
    onChange={(e) => setName(e.target.value)} 
/>

<TextInput
    label="Comment"
    placeholder="Enter a comment..."
    required
    value={comment} 
    className="glass-inputModal"
    style={{ marginBottom: "20px" }}
    onChange={(e) => setComment(e.target.value)} />
      
           <Button  className="add-button glass-button" type="submit" loading={loading}  > Add
           </Button>
                        
                         
                           

    </form>
  );
};

export default AddPartForm;
