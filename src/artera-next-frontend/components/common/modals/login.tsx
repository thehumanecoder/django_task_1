"use client";
import { useState, useEffect } from "react";
import { useForm, FormProvider } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { Button } from "@/components/ui/button";
import { CardHeader, CardContent, CardFooter, CardTitle, CardDescription } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { useAuth } from "@/hooks/useAuth"; // Adjust path as needed
import { z } from "zod";

interface DemoCreateAccountModalProps {
  autoOpen?: boolean;
}

// Define validation schemas using Zod
const registerSchema = z.object({
  email: z.string().email("Invalid email address"),
  profile_handle: z
    .string()
    .regex(/^[a-zA-Z0-9_]+$/, "Profile handle must be alphanumeric or contain underscores only."),
  password: z.string().min(6, "Password must be at least 6 characters long"),
});

const loginSchema = z.object({
  profile_handle: z
    .string()
    .regex(/^[a-zA-Z0-9_]+$/, "Profile handle must be alphanumeric or contain underscores only."),
  password: z.string().min(6, "Password must be at least 6 characters long"),
});

type RegisterFormData = z.infer<typeof registerSchema>;
type LoginFormData = z.infer<typeof loginSchema>;

export function DemoCreateAccountModal({ autoOpen = false }: DemoCreateAccountModalProps) {
  const [isOpen, setIsOpen] = useState(autoOpen);
  const [isCreatingAccount, setIsCreatingAccount] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const { login, register: registerAccount } = useAuth();

  useEffect(() => {
    setIsOpen(autoOpen);
  }, [autoOpen]);

  // Initialize form with registerSchema by default
  const formMethods = useForm<RegisterFormData | LoginFormData>({
    resolver: zodResolver(isCreatingAccount ? registerSchema : loginSchema),
    defaultValues: { email: "", profile_handle: "", password: "" },
  });

  const { register, handleSubmit, formState: { errors }, reset } = formMethods;

  // Switch schemas and reset form when toggling modes
  useEffect(() => {
    reset(); // Clear form fields
  }, [isCreatingAccount, reset]);

  const onSubmit = async (data: RegisterFormData | LoginFormData) => {
    try {
      setError(null); // Clear any previous error
      if (isCreatingAccount) {
        const response = await registerAccount(
          (data as RegisterFormData).email,
          data.password,
          data.profile_handle
        );
        if (response) {
          setIsOpen(false);
        }
      } else {
        await login(data.profile_handle, data.password);
        setIsOpen(false); // Close modal on successful login
      }
    } catch (err) {
      setError("Invalid email, username, or password. Please try again.");
    }
  };

  const toggleMode = () => {
    setIsCreatingAccount((prev) => !prev);
    setError(null);
  };

  if (!isOpen) return null; // Render nothing if modal is closed

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50 backdrop-blur-sm">
      <div className="relative bg-black rounded-lg p-6 w-full max-w-md">
        <FormProvider {...formMethods}>
          <form onSubmit={handleSubmit(onSubmit)}>
            <CardHeader className="space-y-1">
              <CardTitle className="text-2xl text-center">
                {isCreatingAccount ? "Create an account" : "Login to your account"}
              </CardTitle>
              <CardDescription className="text-center">
                Enter your information below to {isCreatingAccount ? "create your account" : "login to your account"}
              </CardDescription>
            </CardHeader>
            <CardContent className="grid gap-4">
              <div className="grid gap-2">
                <Label htmlFor="profile_handle">Username</Label>
                <Input
                  id="profile_handle"
                  type="text"
                  placeholder="profile handle"
                  {...register("profile_handle")}
                />
                {errors.profile_handle && <span className="text-red-500 text-sm">{errors.profile_handle.message}</span>}
              </div>

              {isCreatingAccount && (
                <div className="grid gap-2">
                  <Label htmlFor="email">Email</Label>
                  <Input
                    id="email"
                    type="email"
                    placeholder="m@example.com"
                    {...register("email")}
                  />
                  {errors.email && <span className="text-red-500 text-sm">{errors.email.message}</span>}
                </div>
              )}

              <div className="grid gap-2">
                <Label htmlFor="password">Password</Label>
                <Input
                  id="password"
                  type="password"
                  {...register("password")}
                />
                {errors.password && <span className="text-red-500 text-sm">{errors.password.message}</span>}
              </div>
              {error && <span className="text-red-500 text-sm">{error}</span>}
            </CardContent>
            <CardFooter className="flex flex-col space-y-2">
              <Button
                type="submit"
                className="w-full font-semibold bg-[#F2C14E] text-black py-2 rounded"
              >
                {isCreatingAccount ? "Create Account" : "Login"}
              </Button>
              <Button type="button" variant="link" className="text-sm text-white hover:underline" onClick={toggleMode}>
                {isCreatingAccount ? "Already have an account? Login" : "Don't have an account? Create one"}
              </Button>
            </CardFooter>
          </form>
        </FormProvider>
      </div>
    </div>
  );
}