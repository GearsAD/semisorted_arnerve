/* LCM type definition class file
 * This file was automatically generated by lcm-gen
 * DO NOT MODIFY BY HAND!!!!
 */

using System;
using System.Collections.Generic;
using System.IO;
using LCM.LCM;
 
namespace semisorted_arnerve
{
    public sealed class wearable_update_t : LCM.LCM.LCMEncodable
    {
        public long timestamp;
        public byte issourceupdating;
        public byte numKeysDown;
        public short[] keysPressed;
        public semisorted_arnerve.joystick_update_t joystick;
 
        public wearable_update_t()
        {
        }
 
        public static readonly ulong LCM_FINGERPRINT;
        public static readonly ulong LCM_FINGERPRINT_BASE = 0x27622aafeb64febfL;
 
        static wearable_update_t()
        {
            LCM_FINGERPRINT = _hashRecursive(new List<String>());
        }
 
        public static ulong _hashRecursive(List<String> classes)
        {
            if (classes.Contains("semisorted_arnerve.wearable_update_t"))
                return 0L;
 
            classes.Add("semisorted_arnerve.wearable_update_t");
            ulong hash = LCM_FINGERPRINT_BASE
                 + semisorted_arnerve.joystick_update_t._hashRecursive(classes)
                ;
            classes.RemoveAt(classes.Count - 1);
            return (hash<<1) + ((hash>>63)&1);
        }
 
        public void Encode(LCMDataOutputStream outs)
        {
            outs.Write((long) LCM_FINGERPRINT);
            _encodeRecursive(outs);
        }
 
        public void _encodeRecursive(LCMDataOutputStream outs)
        {
            outs.Write(this.timestamp); 
 
            outs.Write(this.issourceupdating); 
 
            outs.Write(this.numKeysDown); 
 
            for (int a = 0; a < this.numKeysDown; a++) {
                outs.Write(this.keysPressed[a]); 
            }
 
            this.joystick._encodeRecursive(outs); 
 
        }
 
        public wearable_update_t(byte[] data) : this(new LCMDataInputStream(data))
        {
        }
 
        public wearable_update_t(LCMDataInputStream ins)
        {
            if ((ulong) ins.ReadInt64() != LCM_FINGERPRINT)
                throw new System.IO.IOException("LCM Decode error: bad fingerprint");
 
            _decodeRecursive(ins);
        }
 
        public static semisorted_arnerve.wearable_update_t _decodeRecursiveFactory(LCMDataInputStream ins)
        {
            semisorted_arnerve.wearable_update_t o = new semisorted_arnerve.wearable_update_t();
            o._decodeRecursive(ins);
            return o;
        }
 
        public void _decodeRecursive(LCMDataInputStream ins)
        {
            this.timestamp = ins.ReadInt64();
 
            this.issourceupdating = ins.ReadByte();
 
            this.numKeysDown = ins.ReadByte();
 
            this.keysPressed = new short[(int) numKeysDown];
            for (int a = 0; a < this.numKeysDown; a++) {
                this.keysPressed[a] = ins.ReadInt16();
            }
 
            this.joystick = semisorted_arnerve.joystick_update_t._decodeRecursiveFactory(ins);
 
        }
 
        public semisorted_arnerve.wearable_update_t Copy()
        {
            semisorted_arnerve.wearable_update_t outobj = new semisorted_arnerve.wearable_update_t();
            outobj.timestamp = this.timestamp;
 
            outobj.issourceupdating = this.issourceupdating;
 
            outobj.numKeysDown = this.numKeysDown;
 
            outobj.keysPressed = new short[(int) numKeysDown];
            for (int a = 0; a < this.numKeysDown; a++) {
                outobj.keysPressed[a] = this.keysPressed[a];
            }
 
            outobj.joystick = this.joystick.Copy();
 
            return outobj;
        }
    }
}

