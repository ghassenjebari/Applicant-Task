import { useState, useEffect } from 'react';
import { Button, TextInput, Group } from '@mantine/core';
import { updatePart, getPartById } from '@/data/dataHandler';

interface ModifyPartFormProps {
  partId: number;
  onPartUpdated: () => void;  
  onClose: () => void;        
}

const ModifyPartForm: React.FC<ModifyPartFormProps> = ({ partId, onPartUpdated, onClose }) => {
  const [name, setName] = useState<string>('');
  const [comment, setComment] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);

  useEffect(() => {
    const fetchPartDetails = async () => {
      setLoading(true);
      try {
        const part = await getPartById(partId);
        setName(part.name);
        setComment(part.comment);
      } catch (error) {
        console.error('Error fetching part details:', error);
      }
      setLoading(false);
    };

    fetchPartDetails();
  }, [partId]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      await updatePart(partId, { name, comment });
      onPartUpdated();
      onClose(); 
    } catch (error) {
      console.error('Error updating part:', error);
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
        onChange={(e) => setComment(e.target.value)}
      />


<div style={{ display: "flex", gap: "15px", justifyContent: "center" }}>

        <Button
          className="add-button glass-button"
          type="submit"
          loading={loading}
          style={{ marginRight: "10px" }} 

        >
          Update Part
        </Button>
        <Button
          className="add-button glass-button"
          color="red"
          onClick={onClose}         >
          Cancel
        </Button>
  </div>

    </form>
  );
};

export default ModifyPartForm;
